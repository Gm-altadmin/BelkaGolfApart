from pathlib import Path
p=Path(r'c:/Users/pc/bitcolosia/BelkaGolfApart/index.html')
b=p.read_bytes()
methods=[]
# raw utf-8
try:
    s_utf8=b.decode('utf-8')
    methods.append(('utf-8',s_utf8))
except:
    pass
# try re-interpret utf8-decoded bytes as latin1 then decode to candidate encs
candidates=['cp1254','iso-8859-9','cp1252','latin1']
for enc in candidates:
    try:
        s = b.decode('utf-8')
        recovered = s.encode('latin1').decode(enc)
        methods.append((f'utf8->latin1->{enc}',recovered))
    except Exception as ex:
        methods.append((f'fail->{enc}',str(ex)))

for name,text in methods:
    print('====',name,'====')
    sample='\n'.join(text.splitlines()[:10])
    print(sample)
    print('\ncontains common turkish words:', any(w in text for w in ['Lüks','Lüks','Belek','golf','rezervasyon','havuz','sahas']))
    print('\n')
