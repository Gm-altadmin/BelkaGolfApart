from pathlib import Path
p=Path(r'c:/Users/pc/bitcolosia/BelkaGolfApart/index.html')
b=p.read_bytes()
encodings=['utf-8','cp1254','iso-8859-9','cp1252','latin1']
for e in encodings:
    try:
        s=b.decode(e)
        print(f'OK:{e}')
        print('\n--- sample (first 20 lines) ---')
        print('\n'.join(s.splitlines()[:20]))
        break
    except Exception as ex:
        print(f'FAIL:{e}: {ex}')
else:
    print('No encoding succeeded')
