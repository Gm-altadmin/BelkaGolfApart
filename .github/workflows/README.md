# GitHub Adımları (GitHub Actions)

Bu klasör, GitHub Actions iş akışlarını içerir. GitHub, bu YAML dosyalarını otomatik olarak yönetir.

## 📋 Mevcut Workflows

### 1. Deploy to GitHub Pages (`deploy.yml`)
- Kod her push edildiğinde otomatik olarak GitHub Pages'a yayınlanır
- `main` veya `master` branch'i push edilirse çalışır
- Custom domain (belkagolfapart.com) ayarı bulunur

## 🚀 GitHub Pages Aktifleştirme

1. GitHub projesine git
2. Settings → Pages menüsü aç
3. Source: "GitHub Actions" seç
4. Deploy
5. Tarayıcıda `https://kullanici-adi.github.io/belka-golf-website` adresine erişebilirsiniz

## 🔐 Custom Domain Bağlama

1. `deploy.yml` dosyasında `cname:` satırını güncelleyin
2. Domain DNS ayarlarında GitHub IP'lerini ekleyin
3. GitHub Settings → Pages'ta domain adresini ekleyin

---

Detaylı bilgi için: https://docs.github.com/en/actions
