from pathlib import Path
p=Path(r'c:/Users/pc/bitcolosia/BelkaGolfApart/index.html')
b=p.read_bytes()
encodings=['utf-8','cp1254','iso-8859-9','cp1252','latin1']
for e in encodings:
    try:
        s=b.decode(e)
        print('====',e,'====')
        print('\n'.join(s.splitlines()[:10]))
        print('\n')
    except Exception as ex:
        print(f'FAIL:{e}: {ex}')
