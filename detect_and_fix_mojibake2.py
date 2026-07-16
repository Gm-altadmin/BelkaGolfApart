from pathlib import Path
p=Path(r'c:/Users/pc/bitcolosia/BelkaGolfApart/index.html')
b=p.read_bytes()
methods=[]
try:
    s_utf8=b.decode('utf-8')
    s_utf8_stripped = s_utf8.lstrip('\ufeff')
    methods.append(('utf-8',s_utf8_stripped))
except Exception as ex:
    methods.append(('utf-8-fail',str(ex)))

candidates=['cp1254','iso-8859-9','cp1252','latin1']
for enc in candidates:
    try:
        recovered = s_utf8_stripped.encode('latin1',errors='ignore').decode(enc,errors='ignore')
        methods.append((f'utf8->latin1->{enc}',recovered))
    except Exception as ex:
        methods.append((f'fail->{enc}',str(ex)))

for name,text in methods:
    print('====',name,'====')
    print('\n'.join(text.splitlines()[:10]))
    print('\ncontains common turkish words:', any(w in text for w in ['Lüks','Lüks','Belek','golf','rezervasyon','havuz','saha','sahası','sahas']))
    print('\n')
