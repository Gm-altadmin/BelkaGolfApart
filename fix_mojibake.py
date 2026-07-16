from pathlib import Path
p=Path(r'c:/Users/pc/bitcolosia/BelkaGolfApart/index.html')
s=p.read_text(encoding='utf-8')
repls={
    'Ã¼':'ü','Ãœ':'Ü','Ã§':'ç','Ã‡':'Ç','Ã¶':'ö','Ã–':'Ö','ÅŸ':'ş','Åž':'Ş','Ä±':'ı',
    'â€“':'–','â€”':'—','â€˜':'‘','â€™':'’','â€œ':'“','â€�':'”','Â':'',
    'Ã¢â‚¬â„¢':'’','Ã¢â€šâ€˜':'‘','ÃƒÂ¼':'ü','Ã‚Â':'',
}
for a,b in repls.items():
    s=s.replace(a,b)
out=Path('index_fixed.html')
out.write_text(s,encoding='utf-8')
print('Wrote',out)
print('\n--- sample ---')
print('\n'.join(s.splitlines()[:20]))
