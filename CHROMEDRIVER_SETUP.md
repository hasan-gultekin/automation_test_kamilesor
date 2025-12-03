# ChromeDriver Kurulum Talimatları

## Adım 1: Chrome Sürümünüzü Öğrenin

1. Chrome tarayıcısını açın
2. Adres çubuğuna `chrome://version` yazın
3. İlk satırdaki sürüm numarasını not edin

## Adım 2: ChromeDriver İndirin

### Chrome 115 ve Üzeri
[Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) adresinden:
- Stable → chromedriver → win64 linkini kullanın

### Chrome 114 ve Altı
[ChromeDriver Arşivi](https://chromedriver.chromium.org/downloads)

## Adım 3: Kurulum

1. ZIP dosyasını açın
2. `chromedriver.exe` dosyasını proje kök dizinine kopyalayın

```
kamile_sor_test/
├── chromedriver.exe  ← Buraya
├── pages/
├── tests/
└── ...
```

## Sorun Giderme

**Sürüm uyumsuzluğu:**
- Chrome ve ChromeDriver major versiyonları aynı olmalı (örn: 142.x)

**Sistem politikası hatası:**
- Manuel ChromeDriver kullanın (otomatik indirme yerine)
