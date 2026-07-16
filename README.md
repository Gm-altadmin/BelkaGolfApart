# рџЏЁ Belka Golf Residence - Belek, Antalya

Modern ve responsive web sitesi - Belka Golf Residence lГјks apart tatil kompleksi iГ§in tasarlanmД±Еџ profesyonel tanД±tД±m sitesi.

## рџ“‹ Proje HakkД±nda

Belka Golf Residence, Belek'in kalbinde, golf sahasД± yanД±nda konumlanmД±Еџ ve havuzlu, tam donanД±mlД± lГјks apart daireler sunmaktadД±r. Bu proje, iЕџletmenin Г§evrimiГ§i varlД±ДџД±nД± gГјГ§lendirmek iГ§in geliЕџtirilmiЕџtir.

### вњЁ Г–zellikler

- **рџ“± Responsive TasarД±m** - Mobil, tablet ve masaГјstГј cihazlara tam uyumlu
- **рџЊЌ Г‡ok Dil DesteДџi** - TR, EN, DE, RU dil seГ§enekleri
- **рџЋЇ SEO Optimized** - Schema.org JSON-LD yapД±landД±rД±lmД±Еџ veri
- **вњЁ Smooth Animasyonlar** - CSS animasyonlarД± ve transitions
- **рџ“… Rezervasyon Sistemi** - Tarih seГ§imi ve oda tГјrГј seГ§me
- **рџ–јпёЏ Galeri** - CSS Grid masonry galeri dГјzeni
- **в­ђ Platform PuanlarД±** - Booking, Airbnb, Google vb. derecelendirmeler
- **рџ“Ќ Harita Entegrasyonu** - Konum bilgileri
- **рџ’¬ MГјЕџteri YorumlarД±** - 5 yД±ldД±zlД± testimoniallar
- **рџ“ћ WhatsApp Entegrasyonu** - HД±zlД± iletiЕџim FAB

## рџЋЁ TasarД±m Г–zellikleri

- **Font Stack:** 
  - Serif: Cormorant Garamond
  - Sans-serif: Jost
- **Renk ЕћemasД±:**
  - Ana Renk: #b8923a (AltД±n)
  - Arka Plan: #f8f5f0
  - Metni: #1a1a1a
  - YeЕџil (Hero): #0f1a10

## рџ“Ѓ KlasГ¶r YapД±sД±

```
belka-golf-website/
в”њв”Ђв”Ђ index.html           # Ana HTML dosyasД±
в”њв”Ђв”Ђ assets/
в”‚   в”њв”Ђв”Ђ css/
в”‚   в”‚   в””в”Ђв”Ђ styles.css   # TГјm stilleri iГ§erir
в”‚   в”њв”Ђв”Ђ js/
в”‚   в”‚   в”њв”Ђв”Ђ main.js      # Ana JavaScript
в”‚   в”‚   в”њв”Ђв”Ђ i18n.js      # Г‡ok dil desteДџi
в”‚   в”‚   в””в”Ђв”Ђ scroll.js    # Scroll efektleri
в”‚   в””в”Ђв”Ђ images/          # Resim dosyalarД±
в”њв”Ђв”Ђ README.md            # Bu dosya
в”њв”Ђв”Ђ .gitignore           # Git ignore dosyasД±
в”њв”Ђв”Ђ LICENSE              # Lisans
в””в”Ђв”Ђ package.json         # NPM konfigГјrasyonu
```

## рџљЂ Kurulum & Г‡alД±ЕџtД±rma

### 1. Projeyi Clone Et
```bash
git clone https://github.com/kullanici-adi/belka-golf-website.git
cd belka-golf-website
```

### 2. Live Server ile Г‡alД±ЕџtД±r (VS Code)
- VS Code'u aГ§ ve `index.html` dosyasД±nД± aГ§
- "Go Live" butonuna tД±kla (saДџ alt kГ¶Еџede)
- TarayД±cД±da http://localhost:5500 adresinde aГ§Д±lacak

### 3. HTTP Server ile Г‡alД±ЕџtД±r (Python)
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```
ArdД±ndan http://localhost:8000 adresine git

### 4. Node.js http-server Kullan
```bash
npm install -g http-server
http-server
```

## рџ”§ GeliЕџtirme

### Gereklilikler
- Modern web tarayД±cД±sД± (Chrome, Firefox, Safari, Edge)
- Kod editГ¶rГј (VS Code, Sublime Text, vb.)
- Git (sГјrГјm kontrolГј iГ§in)

### Dosya YapД±sД± AГ§Д±klamasД±

| Dosya | AГ§Д±klama |
|-------|----------|
| `index.html` | Ana HTML dosyasД± - tГјm sayfanД±n yapД±sД± |
| `assets/css/styles.css` | CSS stilleri ve responsive dГјzen |
| `assets/js/main.js` | DOM manipГјlasyonu ve interaktif Г¶Дџeler |
| `assets/js/i18n.js` | Г‡ok dil (Internationalization) sistemi |
| `assets/js/scroll.js` | Scroll animasyonlarД± ve navbar efektleri |

## рџ“± Responsive Breakpoints

- **1200px ve ГјstГј** - Desktop
- **992px - 1199px** - Tablet Large
- **768px - 991px** - Tablet
- **576px - 767px** - Mobil Large
- **320px - 575px** - Mobil Small

## рџЊђ Sayfa BГ¶lГјmleri

1. **Navigasyon** - Sabit navbar, logo, linkler, dil seГ§ici
2. **Hero Section** - HoЕџ geldiniz animasyonlu bГ¶lГјm
3. **Rezervasyon BarД±** - Tarih, oda tГјrГј seГ§imi
4. **GiriЕџ** - Д°Еџletme tanД±tД±mД± ve Г¶zellikler
5. **Konum** - Harita ve lokasyon bilgileri
6. **Daireler** - Oda tiplerine gГ¶re kartlar (1+1, 2+1, 3+1)
7. **Havuz BГ¶lГјmГј** - Tesisler gГ¶rseli
8. **Г–zellikler** - Amenities grid
9. **Galeri** - GГ¶rsel galerisi (masonry)
10. **Restaurant (Viking19)** - Restoran tanД±tД±mД±
11. **Platform PuanlarД±** - Booking, Airbnb, Google puanlarД±
12. **MГјЕџteri YorumlarД±** - 5 yД±ldД±zlД± testimoniallar
13. **Footer** - Д°letiЕџim bilgileri ve linkler

## рџЋЇ SEO Г–zelikleri

вњ… Meta title ve description
вњ… Open Graph meta tagleri
вњ… Twitter Card
вњ… Schema.org JSON-LD yapД±landД±rД±lmД±Еџ veri (LodgingBusiness)
вњ… Canonical URL
вњ… robots.txt uyumluluДџu
вњ… Mobile-friendly viewport

## рџ”— BaДџlantД±lar

- **Website:** https://belkagolfapart.com
- **Email:** info@belkagolf.com
- **Telefon:** +90-532-262-27-73
- **Adres:** Belek Mah. Mehmet Akif Ersoy Cad. 25, Belek, Antalya, TR

## рџ“„ Lisans

Bu proje [MIT LisansД±](LICENSE) altД±nda yayД±nlanmД±ЕџtД±r.

## рџ¤ќ KatkД±da Bulunma

KatkД±lar memnuniyetle karЕџД±lanД±r! LГјtfen:

1. Projeyi fork et
2. Feature branch oluЕџtur (`git checkout -b feature/AmazingFeature`)
3. DeДџiЕџiklikleri commit et (`git commit -m 'Add some AmazingFeature'`)
4. Branch'i push et (`git push origin feature/AmazingFeature`)
5. Pull Request aГ§

## рџ“§ Д°letiЕџim

SorularД±nД±z iГ§in bize ulaЕџД±n:
- **Email:** info@belkagolf.com
- **WhatsApp:** [WhatsApp Гјzerinden iletiЕџim](https://wa.me/905322622773)

---

Made with вќ¤пёЏ by Belka Golf Residence Team
