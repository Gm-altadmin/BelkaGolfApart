# GitHub AdД±mlarД± (GitHub Actions)

Bu klasГ¶r, GitHub Actions iЕџ akД±ЕџlarД±nД± iГ§erir. GitHub, bu YAML dosyalarД±nД± otomatik olarak yГ¶netir.

## рџ“‹ Mevcut Workflows

### 1. Deploy to GitHub Pages (`deploy.yml`)
- Kod her push edildiДџinde otomatik olarak GitHub Pages'a yayД±nlanД±r
- `main` veya `master` branch'i push edilirse Г§alД±ЕџД±r
- Custom domain (belkagolfapart.com) ayarД± bulunur

## рџљЂ GitHub Pages AktifleЕџtirme

1. GitHub projesine git
2. Settings в†’ Pages menГјsГј aГ§
3. Source: "GitHub Actions" seГ§
4. Deploy
5. TarayД±cД±da `https://kullanici-adi.github.io/belka-golf-website` adresine eriЕџebilirsiniz

## рџ”ђ Custom Domain BaДџlama

1. `deploy.yml` dosyasД±nda `cname:` satД±rД±nД± gГјncelleyin
2. Domain DNS ayarlarД±nda GitHub IP'lerini ekleyin
3. GitHub Settings в†’ Pages'ta domain adresini ekleyin

---

DetaylД± bilgi iГ§in: https://docs.github.com/en/actions
