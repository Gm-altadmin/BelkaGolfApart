# 🚀 GitHub'a Proje Yükleme Rehberi

Bu rehber, Belka Golf Website projesini GitHub'a nasıl yükleyeceğinizi adım adım anlatır.

## 📋 Ön Gereklilikler

- GitHub hesabı (https://github.com adresinden kaydolun)
- Git kurulu (https://git-scm.com adresinden indirin)
- Terminal/PowerShell bilgisi

## 🔧 1. Adım: GitHub Deposu Oluştur

1. GitHub'da oturum aç
2. Sağ üst köşede "+" butonuna tıkla → "New repository"
3. Repository adını yaz: `belka-golf-website`
4. Açıklama yaz: `Belka Golf Residence - Responsive Website`
5. Public seç (diğerleri tarafından görülebilsin)
6. ✅ **Create repository** butonuna tıkla

## 💻 2. Adım: Projeyi Initialize Et

Proje klasöründe Terminal açın ve şunları yazın:

```bash
# Proje klasörine git
cd c:\Users\PC\Downloads\belka-golf-website

# Git'i initialize et
git init

# Varsayılan branch'i main yapın
git branch -M main

# Tüm dosyaları staging alanına ekle
git add .

# İlk commit oluştur
git commit -m "Initial commit: Belka Golf Website"

# GitHub reposunu uzaktan ekle
git remote add origin https://github.com/KULLANICI-ADIN/belka-golf-website.git

# Kodu GitHub'a push et
git push -u origin main
```

## 🔑 3. Adım: GitHub Credentials Ayarla (İlk Kez)

Windows'ta token kullanmanız gerekebilir:

```bash
# Git config ayarla
git config --global user.name "Adın Soyadın"
git config --global user.email "email@example.com"
```

### GitHub Personal Access Token (PAT) Oluştur:

1. GitHub'da sağ üst profil → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)" tıkla
3. Token adını yaz: "belka-golf-website"
4. Scopes seç: `repo`, `workflow`
5. Token oluştur ve **kopyala** (bir kez görüntülenir!)
6. Terminal'e sorduğunda bu token'ı yapıştır

## 📤 4. Adım: Kod Yükle

```bash
# Tüm dosyaları ekle
git add .

# Commit oluştur
git commit -m "Add project structure and documentation"

# GitHub'a gönder
git push origin main
```

## ✨ 5. Adım: GitHub Pages Etkinleştir

1. GitHub'daki proje sayfasına git
2. **Settings** butonuna tıkla
3. Sol taraftan **Pages** seç
4. Source: "GitHub Actions" seç
5. Biraz bekle, sayfanız otomatik yayınlanacak
6. `https://kullanici-adin.github.io/belka-golf-website` adresinde açılacak

## 🌐 6. Adım: Custom Domain Bağla (Opsiyonel)

Eğer belkagolfapart.com'u bağlamak istiyorsanız:

1. Domenin DNS ayarlarına git (domain sağlayıcısı panelinde)
2. GitHub'ın DNS kayıtlarını ekle (GitHub Settings → Pages'ta belirtilir)
3. GitHub'da domain adresini ekle
4. CNAME dosyası otomatik oluşturulacak

## 📝 7. Adım: README Dosyasını Özelleştir

1. `README.md` dosyasını düzenle
2. Kendi bilgilerinizi ekle
3. Commit ve push et

```bash
git add README.md
git commit -m "Update README with project details"
git push origin main
```

## 🔄 8. Adım: İlerideki Güncellemeler

Her seferinde aynı adımları takip edin:

```bash
# 1. Dosyaları düzenle

# 2. Değişiklikleri add et
git add .

# 3. Commit oluştur
git commit -m "Açıklamalı commit mesajı"

# 4. Push et
git push origin main
```

## 📊 Faydalı Git Komutları

```bash
# Durumu kontrol et
git status

# Son commitlari göster
git log

# Dosya değişikliklerini geri al
git restore <dosya-adı>

# Son commiti geri al
git reset --soft HEAD~1

# Remote'u kontrol et
git remote -v

# Branch'ler listesi
git branch -a
```

## 🐛 Sorun Giderme

### "fatal: invalid username/password"
- Token'ı doğru yazıp yazmadığınızı kontrol edin
- Token'ı GitHub'da yenile

### "Please tell me who you are"
```bash
git config --global user.name "Adın"
git config --global user.email "email@example.com"
```

### Dosyalar push edilmiyor
```bash
# Durumu kontrol et
git status

# Hangi dosyalar değişti göster
git diff
```

## 📞 Daha Fazla Yardım

- GitHub Docs: https://docs.github.com
- Git Rehberi: https://git-scm.com/book/tr/v2
- GitHub Actions: https://docs.github.com/en/actions

---

Başarıyla tamamladınız! 🎉 Projeniz şimdi GitHub'da ve GitHub Pages'ta yayında! 🚀
