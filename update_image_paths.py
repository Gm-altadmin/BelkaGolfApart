from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
replacements = {
    '<img src="images/havuzhero.webp" alt="1+1 Exclusive Poolside"/>':'<img src="images/havuz4.webp" alt="1+1 Exclusive Poolside"/>',
    '<img src="images/havuzhero.webp" alt="2+1 Deluxe Poolside"/>':'<img src="images/salon1.webp" alt="2+1 Deluxe Poolside"/>',
    '<img src="images/havuzhero.webp" alt="3+1 Dublex Apt."/>':'<img src="images/yatak4.webp" alt="3+1 Dublex Apt."/>',
    '<img src="images/havuzhero.webp" alt="Apartman Dýþ Cephe"/>':'<img src="images/dis12.webp" alt="Apartman Dýþ Cephe"/>',
    '<img src="images/havuzhero.webp" alt="Yatak Odasý"/>':'<img src="images/yatak3.webp" alt="Yatak Odasý"/>',
    '<img src="images/havuzhero.webp" alt="Balkon"/>':'<img src="images/park1.webp" alt="Balkon"/>',
    '<img src="images/havuzhero.webp" alt="Banyo"/>':'<img src="images/sauna2.webp" alt="Banyo"/>',
    '<img src="images/havuzhero.webp" alt="Golf Sahasý Manzarasý"/>':'<img src="images/havuz9.webp" alt="Golf Sahasý Manzarasý"/>',
    '<img src="images/havuz20.webp" alt="Bahçe"/>':'<img src="images/park1.webp" alt="Bahçe"/>',
    '<img src="images/havuz20.webp" alt="Oturma Odasý"/>':'<img src="images/salon3.webp" alt="Oturma Odasý"/>',
    '<img src="images/havuz20.webp" alt="Mutfak"/>':'<img src="images/salon4.webp" alt="Mutfak"/>',
    '<img src="images/havuz20.webp" alt="Teras"/>':'<img src="images/havuz2.webp" alt="Teras"/>',
    '<img src="images/havuz20.webp" alt="Gece Manzarasý"/>':'<img src="images/havuz17.webp" alt="Gece Manzarasý"/>'
}
for old, new in replacements.items():
    text = text.replace(old, new)
p.write_text(text, encoding='utf-8')
print('done')
