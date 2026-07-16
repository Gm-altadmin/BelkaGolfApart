# СЂСџС™Р‚ GitHub'a Proje YР“С�kleme Rehberi

Bu rehber, Belka Golf Website projesini GitHub'a nasР”В±l yР“С�kleyeceР”Сџinizi adР”В±m adР”В±m anlatР”В±r.

## СЂСџвЂњвЂ№ Р“вЂ“n Gereklilikler

- GitHub hesabР”В± (https://github.com adresinden kaydolun)
- Git kurulu (https://git-scm.com adresinden indirin)
- Terminal/PowerShell bilgisi

## СЂСџвЂќВ§ 1. AdР”В±m: GitHub Deposu OluР•Сџtur

1. GitHub'da oturum aР“В§
2. SaР”Сџ Р“С�st kР“В¶Р•Сџede "+" butonuna tР”В±kla РІвЂ вЂ™ "New repository"
3. Repository adР”В±nР”В± yaz: `belka-golf-website`
4. AР“В§Р”В±klama yaz: `Belka Golf Residence - Responsive Website`
5. Public seР“В§ (diР”Сџerleri tarafР”В±ndan gР“В¶rР“С�lebilsin)
6. РІСљвЂ¦ **Create repository** butonuna tР”В±kla

## СЂСџвЂ™В» 2. AdР”В±m: Projeyi Initialize Et

Proje klasР“В¶rР“С�nde Terminal aР“В§Р”В±n ve Р•СџunlarР”В± yazР”В±n:

```bash
# Proje klasР“В¶rine git
cd c:\Users\PC\Downloads\belka-golf-website

# Git'i initialize et
git init

# VarsayР”В±lan branch'i main yapР”В±n
git branch -M main

# TР“С�m dosyalarР”В± staging alanР”В±na ekle
git add .

# Р”В°lk commit oluР•Сџtur
git commit -m "Initial commit: Belka Golf Website"

# GitHub reposunu uzaktan ekle
git remote add origin https://github.com/KULLANICI-ADIN/belka-golf-website.git

# Kodu GitHub'a push et
git push -u origin main
```

## СЂСџвЂќвЂ� 3. AdР”В±m: GitHub Credentials Ayarla (Р”В°lk Kez)

Windows'ta token kullanmanР”В±z gerekebilir:

```bash
# Git config ayarla
git config --global user.name "AdР”В±n SoyadР”В±n"
git config --global user.email "email@example.com"
```

### GitHub Personal Access Token (PAT) OluР•Сџtur:

1. GitHub'da saР”Сџ Р“С�st profil РІвЂ вЂ™ Settings РІвЂ вЂ™ Developer settings РІвЂ вЂ™ Personal access tokens РІвЂ вЂ™ Tokens (classic)
2. "Generate new token (classic)" tР”В±kla
3. Token adР”В±nР”В± yaz: "belka-golf-website"
4. Scopes seР“В§: `repo`, `workflow`
5. Token oluР•Сџtur ve **kopyala** (bir kez gР“В¶rР“С�ntР“С�lenir!)
6. Terminal'e sorduР”Сџunda bu token'Р”В± yapР”В±Р•СџtР”В±r

## СЂСџвЂњВ¤ 4. AdР”В±m: Kod YР“С�kle

```bash
# TР“С�m dosyalarР”В± ekle
git add .

# Commit oluР•Сџtur
git commit -m "Add project structure and documentation"

# GitHub'a gР“В¶nder
git push origin main
```

## РІСљРЃ 5. AdР”В±m: GitHub Pages EtkinleР•Сџtir

1. GitHub'daki proje sayfasР”В±na git
2. **Settings** butonuna tР”В±kla
3. Sol taraftan **Pages** seР“В§
4. Source: "GitHub Actions" seР“В§
5. Biraz bekle, sayfanР”В±z otomatik yayР”В±nlanacak
6. `https://kullanici-adin.github.io/belka-golf-website` adresinde aР“В§Р”В±lacak

## СЂСџРЉС’ 6. AdР”В±m: Custom Domain BaР”Сџla (Opsiyonel)

EР”Сџer belkagolfapart.com'u baР”Сџlamak istiyorsanР”В±z:

1. Domenin DNS ayarlarР”В±na git (domain saР”СџlayР”В±cР”В±sР”В± panelinde)
2. GitHub'Р”В±n DNS kayР”В±tlarР”В±nР”В± ekle (GitHub Settings РІвЂ вЂ™ Pages'ta belirtilir)
3. GitHub'da domain adresini ekle
4. CNAME dosyasР”В± otomatik oluР•Сџturulacak

## СЂСџвЂњСњ 7. AdР”В±m: README DosyasР”В±nР”В± Р“вЂ“zelleР•Сџtir

1. `README.md` dosyasР”В±nР”В± dР“С�zenle
2. Kendi bilgilerinizi ekle
3. Commit ve push et

```bash
git add README.md
git commit -m "Update README with project details"
git push origin main
```

## СЂСџвЂќвЂћ 8. AdР”В±m: Р”В°lerideki GР“С�ncellemeler

Her seferinde aynР”В± adР”В±mlarР”В± takip edin:

```bash
# 1. DosyalarР”В± dР“С�zenle

# 2. DeР”СџiР•Сџiklikleri add et
git add .

# 3. Commit oluР•Сџtur
git commit -m "AР“В§Р”В±klamalР”В± commit mesajР”В±"

# 4. Push et
git push origin main
```

## СЂСџвЂњР‰ FaydalР”В± Git KomutlarР”В±

```bash
# Durumu kontrol et
git status

# Son commitlari gР“В¶ster
git log

# Dosya deР”СџiР•Сџikliklerini geri al
git restore <dosya-adР”В±>

# Son commiti geri al
git reset --soft HEAD~1

# Remote'u kontrol et
git remote -v

# Branch'ler listesi
git branch -a
```

## СЂСџС’вЂє Sorun Giderme

### "fatal: invalid username/password"
- Token'Р”В± doР”Сџru yazР”В±p yazmadР”В±Р”СџР”В±nР”В±zР”В± kontrol edin
- Token'Р”В± GitHub'da yenile

### "Please tell me who you are"
```bash
git config --global user.name "AdР”В±n"
git config --global user.email "email@example.com"
```

### Dosyalar push edilmiyor
```bash
# Durumu kontrol et
git status

# Hangi dosyalar deР”СџiР•Сџti gР“В¶ster
git diff
```

## СЂСџвЂњС› Daha Fazla YardР”В±m

- GitHub Docs: https://docs.github.com
- Git Rehberi: https://git-scm.com/book/tr/v2
- GitHub Actions: https://docs.github.com/en/actions

---

BaР•СџarР”В±yla tamamladР”В±nР”В±z! СЂСџР‹вЂ° Projeniz Р•Сџimdi GitHub'da ve GitHub Pages'ta yayР”В±nda! СЂСџС™Р‚
