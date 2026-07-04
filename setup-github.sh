#!/usr/bin/env bash

# Belka Golf Website - GitHub Setup Script
# Bu script, projeyi GitHub'a otomatik olarak hazırlar

echo "🚀 Belka Golf Website - GitHub Setup Başladı"
echo "============================================"

# Git kurulu mu kontrol et
if ! command -v git &> /dev/null; then
    echo "❌ Git yüklü değil! https://git-scm.com adresinden indirin."
    exit 1
fi

echo "✅ Git kurulu"

# Git'i initialize et
echo "📦 Git initializing..."
git init

# Branch'i main yap
git branch -M main

# User config
echo "👤 Git config ayarlanıyor..."
git config user.name "${GIT_USER_NAME:-Belka Golf Team}"
git config user.email "${GIT_EMAIL:-info@belkagolf.com}"

# Dosyaları ekle
echo "📝 Dosyalar ekleniyor..."
git add .

# İlk commit
echo "💾 İlk commit oluşturuluyor..."
git commit -m "Initial commit: Belka Golf Website - Professional Resort Landing Page"

echo ""
echo "✅ Başarılı!"
echo ""
echo "📌 Sonraki Adımlar:"
echo "1. GitHub'da yeni repository oluşturun: https://github.com/new"
echo "2. Repository adını giriniz: belka-golf-website"
echo "3. Aşağıdaki komutları çalıştırın:"
echo ""
echo "   git remote add origin https://github.com/KULLANICI-ADIN/belka-golf-website.git"
echo "   git push -u origin main"
echo ""
echo "4. GitHub Settings → Pages → Source: GitHub Actions"
echo "5. Sayfanız yayında! 🎉"
echo ""
