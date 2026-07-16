# рџљЂ GitHub'a Proje YГјkleme Rehberi

Bu rehber, Belka Golf Website projesini GitHub'a nasД±l yГјkleyeceДџinizi adД±m adД±m anlatД±r.

## рџ“‹ Г–n Gereklilikler

- GitHub hesabД± (https://github.com adresinden kaydolun)
- Git kurulu (https://git-scm.com adresinden indirin)
- Terminal/PowerShell bilgisi

## рџ”§ 1. AdД±m: GitHub Deposu OluЕџtur

1. GitHub'da oturum aГ§
2. SaДџ Гјst kГ¶Еџede "+" butonuna tД±kla в†’ "New repository"
3. Repository adД±nД± yaz: `belka-golf-website`
4. AГ§Д±klama yaz: `Belka Golf Residence - Responsive Website`
5. Public seГ§ (diДџerleri tarafД±ndan gГ¶rГјlebilsin)
6. вњ… **Create repository** butonuna tД±kla

## рџ’» 2. AdД±m: Projeyi Initialize Et

Proje klasГ¶rГјnde Terminal aГ§Д±n ve ЕџunlarД± yazД±n:

```bash
# Proje klasГ¶rine git
cd c:\Users\PC\Downloads\belka-golf-website

# Git'i initialize et
git init

# VarsayД±lan branch'i main yapД±n
git branch -M main

# TГјm dosyalarД± staging alanД±na ekle
git add .

# Д°lk commit oluЕџtur
git commit -m "Initial commit: Belka Golf Website"

# GitHub reposunu uzaktan ekle
git remote add origin https://github.com/KULLANICI-ADIN/belka-golf-website.git

# Kodu GitHub'a push et
git push -u origin main
```

## рџ”‘ 3. AdД±m: GitHub Credentials Ayarla (Д°lk Kez)

Windows'ta token kullanmanД±z gerekebilir:

```bash
# Git config ayarla
git config --global user.name "AdД±n SoyadД±n"
git config --global user.email "email@example.com"
```

### GitHub Personal Access Token (PAT) OluЕџtur:

1. GitHub'da saДџ Гјst profil в†’ Settings в†’ Developer settings в†’ Personal access tokens в†’ Tokens (classic)
2. "Generate new token (classic)" tД±kla
3. Token adД±nД± yaz: "belka-golf-website"
4. Scopes seГ§: `repo`, `workflow`
5. Token oluЕџtur ve **kopyala** (bir kez gГ¶rГјntГјlenir!)
6. Terminal'e sorduДџunda bu token'Д± yapД±ЕџtД±r

## рџ“¤ 4. AdД±m: Kod YГјkle

```bash
# TГјm dosyalarД± ekle
git add .

# Commit oluЕџtur
git commit -m "Add project structure and documentation"

# GitHub'a gГ¶nder
git push origin main
```

## вњЁ 5. AdД±m: GitHub Pages EtkinleЕџtir

1. GitHub'daki proje sayfasД±na git
2. **Settings** butonuna tД±kla
3. Sol taraftan **Pages** seГ§
4. Source: "GitHub Actions" seГ§
5. Biraz bekle, sayfanД±z otomatik yayД±nlanacak
6. `https://kullanici-adin.github.io/belka-golf-website` adresinde aГ§Д±lacak

## рџЊђ 6. AdД±m: Custom Domain BaДџla (Opsiyonel)

EДџer belkagolfapart.com'u baДџlamak istiyorsanД±z:

1. Domenin DNS ayarlarД±na git (domain saДџlayД±cД±sД± panelinde)
2. GitHub'Д±n DNS kayД±tlarД±nД± ekle (GitHub Settings в†’ Pages'ta belirtilir)
3. GitHub'da domain adresini ekle
4. CNAME dosyasД± otomatik oluЕџturulacak

## рџ“ќ 7. AdД±m: README DosyasД±nД± Г–zelleЕџtir

1. `README.md` dosyasД±nД± dГјzenle
2. Kendi bilgilerinizi ekle
3. Commit ve push et

```bash
git add README.md
git commit -m "Update README with project details"
git push origin main
```

## рџ”„ 8. AdД±m: Д°lerideki GГјncellemeler

Her seferinde aynД± adД±mlarД± takip edin:

```bash
# 1. DosyalarД± dГјzenle

# 2. DeДџiЕџiklikleri add et
git add .

# 3. Commit oluЕџtur
git commit -m "AГ§Д±klamalД± commit mesajД±"

# 4. Push et
git push origin main
```

## рџ“Љ FaydalД± Git KomutlarД±

```bash
# Durumu kontrol et
git status

# Son commitlari gГ¶ster
git log

# Dosya deДџiЕџikliklerini geri al
git restore <dosya-adД±>

# Son commiti geri al
git reset --soft HEAD~1

# Remote'u kontrol et
git remote -v

# Branch'ler listesi
git branch -a
```

## рџђ› Sorun Giderme

### "fatal: invalid username/password"
- Token'Д± doДџru yazД±p yazmadД±ДџД±nД±zД± kontrol edin
- Token'Д± GitHub'da yenile

### "Please tell me who you are"
```bash
git config --global user.name "AdД±n"
git config --global user.email "email@example.com"
```

### Dosyalar push edilmiyor
```bash
# Durumu kontrol et
git status

# Hangi dosyalar deДџiЕџti gГ¶ster
git diff
```

## рџ“ћ Daha Fazla YardД±m

- GitHub Docs: https://docs.github.com
- Git Rehberi: https://git-scm.com/book/tr/v2
- GitHub Actions: https://docs.github.com/en/actions

---

BaЕџarД±yla tamamladД±nД±z! рџЋ‰ Projeniz Еџimdi GitHub'da ve GitHub Pages'ta yayД±nda! рџљЂ
