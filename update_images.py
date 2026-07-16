from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
replacements = {
    'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/XjlgERNtbZurPaFl/havuz1-rarRaPIkjPZQEwnp.webp': 'images/havuzhero.webp',
    'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1920,fit=crop/XjlgERNtbZurPaFl/belka-golf-residence-belek-havuz.jpg': 'images/havuz20.webp',
    "background: url('viking19-restaurant-belek-belka-golf.jpg') center / cover no-repeat;": "background: url('images/park1.webp') center / cover no-repeat;"
}
for old, new in replacements.items():
    text = text.replace(old, new)
p.write_text(text, encoding='utf-8')
print('updated', len(replacements))
