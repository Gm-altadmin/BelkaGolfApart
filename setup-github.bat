@echo off
REM Belka Golf Website - GitHub Setup Script (Windows)
REM Bu script, projeyi GitHub'a otomatik olarak hazırlar

echo.
echo 🚀 Belka Golf Website - GitHub Setup Başladı
echo ============================================
echo.

REM Git kurulu mu kontrol et
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git yüklü değil! https://git-scm.com adresinden indirin.
    pause
    exit /b 1
)

echo ✅ Git kurulu
echo.

REM Git'i initialize et
echo 📦 Git initializing...
git init
git branch -M main
echo.

REM User config
echo 👤 Git config ayarlanıyor...
git config user.name "Belka Golf Team"
git config user.email "info@belkagolf.com"
echo.

REM Dosyaları ekle
echo 📝 Dosyalar ekleniyor...
git add .
echo.

REM İlk commit
echo 💾 İlk commit oluşturuluyor...
git commit -m "Initial commit: Belka Golf Website - Professional Resort Landing Page"
echo.

echo ✅ Başarılı!
echo.
echo 📌 Sonraki Adımlar:
echo 1. GitHub'da yeni repository oluşturun: https://github.com/new
echo 2. Repository adını giriniz: belka-golf-website
echo 3. Aşağıdaki komutları çalıştırın:
echo.
echo    git remote add origin https://github.com/KULLANICI-ADIN/belka-golf-website.git
echo    git push -u origin main
echo.
echo 4. GitHub Settings ^> Pages ^> Source: GitHub Actions
echo 5. Sayfanız yayında! 🎉
echo.
pause
