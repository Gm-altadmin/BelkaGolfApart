from pathlib import Path
import re

EXTS = ['.html','.htm','.js','.json','.md','.txt']
root = Path('c:/Users/pc/bitcolosia/BelkaGolfApart')
files = [p for p in root.rglob('*') if p.suffix.lower() in EXTS]

def count_cyr(s):
    return sum(1 for ch in s if '\u0400' <= ch <= '\u04FF')

modified = []
for p in files:
    b = p.read_bytes()
    try:
        orig = b.decode('utf-8')
    except Exception:
        orig = b.decode('utf-8',errors='replace')
    orig_c = count_cyr(orig)
    # candidates
    candidates = {}
    # direct cp1251
    try:
        cp1251 = b.decode('cp1251')
        candidates['cp1251_direct'] = cp1251
    except Exception:
        candidates['cp1251_direct'] = b.decode('cp1251',errors='replace')
    # utf8->latin1->cp1251
    try:
        u = b.decode('utf-8')
        cand = u.encode('latin1',errors='replace').decode('cp1251',errors='replace')
        candidates['utf8->latin1->cp1251'] = cand
    except Exception:
        candidates['utf8->latin1->cp1251'] = ''
    # latin1->cp1251
    try:
        lat = b.decode('latin1')
        cand2 = lat.encode('latin1',errors='replace').decode('cp1251',errors='replace')
        candidates['latin1->cp1251'] = cand2
    except Exception:
        candidates['latin1->cp1251']=''

    # evaluate best candidate
    best_method = None
    best_text = orig
    best_score = orig_c
    for m,txt in candidates.items():
        c = count_cyr(txt)
        if c > best_score:
            best_score = c
            best_method = m
            best_text = txt
    if best_method and best_score>=5:
        # apply fix: backup and write utf-8
        bak = p.with_suffix(p.suffix + '.bak_encoding')
        p.rename(bak)
        p.write_text(best_text,encoding='utf-8')
        modified.append((str(p),best_method,best_score))
        print('Fixed',p,'method',best_method,'cyrillic_count',best_score)

print('\nDone. Modified',len(modified),'files')
