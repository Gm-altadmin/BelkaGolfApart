# GitHub AdР”В±mlarР”В± (GitHub Actions)

Bu klasР“В¶r, GitHub Actions iР•Сџ akР”В±Р•СџlarР”В±nР”В± iР“В§erir. GitHub, bu YAML dosyalarР”В±nР”В± otomatik olarak yР“В¶netir.

## СЂСџвЂњвЂ№ Mevcut Workflows

### 1. Deploy to GitHub Pages (`deploy.yml`)
- Kod her push edildiР”Сџinde otomatik olarak GitHub Pages'a yayР”В±nlanР”В±r
- `main` veya `master` branch'i push edilirse Р“В§alР”В±Р•СџР”В±r
- Custom domain (belkagolfapart.com) ayarР”В± bulunur

## СЂСџС™Р‚ GitHub Pages AktifleР•Сџtirme

1. GitHub projesine git
2. Settings РІвЂ вЂ™ Pages menР“С�sР“С� aР“В§
3. Source: "GitHub Actions" seР“В§
4. Deploy
5. TarayР”В±cР”В±da `https://kullanici-adi.github.io/belka-golf-website` adresine eriР•Сџebilirsiniz

## СЂСџвЂќС’ Custom Domain BaР”Сџlama

1. `deploy.yml` dosyasР”В±nda `cname:` satР”В±rР”В±nР”В± gР“С�ncelleyin
2. Domain DNS ayarlarР”В±nda GitHub IP'lerini ekleyin
3. GitHub Settings РІвЂ вЂ™ Pages'ta domain adresini ekleyin

---

DetaylР”В± bilgi iР“В§in: https://docs.github.com/en/actions
