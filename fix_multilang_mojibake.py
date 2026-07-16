from pathlib import Path
import re

root=Path('c:/Users/pc/bitcolosia/BelkaGolfApart')
EXTS=['.html','.htm','.js','.json','.md','.txt','.css']
files=[p for p in root.rglob('*') if p.suffix.lower() in EXTS]

# language character sets
turkish=set('çğıöüşÇĞİÖÜŞ')
german=set('äöüßÄÖÜ')
russian_range=(lambda ch: '\u0400'<=ch<='\u04FF')
english_common=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

candidates_enc=[ 'utf-8','cp1254','cp1251','latin1','cp1252','iso-8859-9']

report=[]
modified=[]

for p in files:
    b=p.read_bytes()
    # original decode as utf-8 (safe)
    try:
        orig=b.decode('utf-8')
    except Exception:
        orig=b.decode('utf-8',errors='replace')
    def score_text(s):
        t=sum(1 for ch in s if ch in turkish)
        g=sum(1 for ch in s if ch in german)
        r=sum(1 for ch in s if '\u0400'<=ch<='\u04FF')
        e=sum(1 for ch in s if ch in english_common)
        mojibake_count = s.count('Ã')+s.count('Â')+s.count('â')+s.count('Ä')+s.count('Å')
        # weighted score: prefer higher language chars, penalize mojibake
        return {'tur':t,'ger':g,'rus':r,'eng':e,'moji':mojibake_count,'total': t*3 + g*3 + r*3 + e + ( - mojibake_count*2)}

    orig_score = score_text(orig)
    best= ('utf-8', orig, orig_score['total'], orig_score)

    # try raw decodings
    for enc in candidates_enc:
        try:
            s=b.decode(enc)
        except Exception:
            s=b.decode(enc,errors='replace')
        sc=score_text(s)
        if sc['total']>best[2]:
            best=(enc,s,sc['total'],sc)
    # try round-trip common fix: utf8->latin1->cp1251 etc
    try:
        u=b.decode('utf-8')
        for enc2 in ['cp1251','cp1254','cp1252','iso-8859-9']:
            try:
                s2 = u.encode('latin1',errors='replace').decode(enc2,errors='replace')
                sc=score_text(s2)
                if sc['total']>best[2]:
                    best=(f'utf8->latin1->{enc2}',s2,sc['total'],sc)
            except Exception:
                pass
    except Exception:
        pass

    # decide
    orig_total=orig_score['total']
    if best[2]>orig_total+5: # significant improvement
        bak=p.with_suffix(p.suffix+'.bak_encoding')
        if not bak.exists():
            p.rename(bak)
        p.write_text(best[1],encoding='utf-8')
        modified.append((str(p),best[0],best[3]))
        report.append(f"Fixed {p} using {best[0]} score {best[2]} (orig {orig_total})")

# summary
print('Files scanned:',len(files))
print('Modified:',len(modified))
for m in modified:
    print(m[0], m[1], m[2])
