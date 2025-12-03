# Kamile Sor Test Otomasyonu

Bu proje, https://kamilesor.com sitesinde kayıt olma işlemini test etmek için Selenium ve Python kullanılarak oluşturulmuş bir test otomasyon projesidir.

## Proje Yapısı

```
kamile_sor_test/
├── pages/                          # Page Object Model dosyaları
│   ├── __init__.py
│   ├── base_page.py               # Temel sayfa sınıfı
│   └── registration_page.py       # Kayıt sayfası Page Object
├── tests/                          # Test dosyaları
│   ├── __init__.py
│   ├── test_registration.py       # Kayıt testleri
│   └── screenshots/               # Test ekran görüntüleri
├── utils/                          # Yardımcı fonksiyonlar
│   ├── __init__.py
│   ├── driver_helper.py           # WebDriver yönetimi
│   └── test_data_helper.py        # Test verisi oluşturma
├── config.py                       # Yapılandırma dosyası
├── requirements.txt                # Python bağımlılıkları
├── pytest.ini                      # Pytest yapılandırması
├── chromedriver.exe               # Chrome WebDriver
└── README.md                       # Bu dosya
```

## Kurulum

1. Python 3.8+ yüklü olduğundan emin olun.

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. ChromeDriver'ı indirin ve proje kök dizinine yerleştirin:
   - Chrome sürümünüzü kontrol edin: `chrome://version`
   - Uygun ChromeDriver'ı indirin: https://googlechromelabs.github.io/chrome-for-testing/
   - `chromedriver.exe` dosyasını proje kök dizinine kopyalayın

## Kullanım

### 1. Locator'ları Güncelleme

Test kodlarını çalıştırmadan önce, gerçek site yapısına göre locator'ları güncellemeniz gerekmektedir:

- `page_objects/registration_page.py` dosyasındaki locator'ları düzenleyin
- Tarayıcınızın Developer Tools'unu kullanarak elementlerin ID, class veya XPath değerlerini bulun

### 2. Testleri Çalıştırma

**Temel test:**
```bash
pytest test_registration.py -v -s
```

**Page Object Model ile test:**
```bash
pytest test_registration_pom.py -v -s
```

**Tüm testleri çalıştır:**
```bash
pytest -v -s
```

### 3. Yapılandırma

`config.py` dosyasından aşağıdaki ayarları değiştirebilirsiniz:
- `BASE_URL`: Test edilecek site URL'i
- `BROWSER`: Kullanılacak tarayıcı (chrome, firefox, edge)
- `IMPLICIT_WAIT`: Örtük bekleme süresi (saniye)
- `EXPLICIT_WAIT`: Açık bekleme süresi (saniye)

## Önemli Notlar

1. **Locator'lar**: Test kodlarındaki element locator'ları (ID, XPath, vb.) örnek olarak verilmiştir. Gerçek site yapısına göre güncellemeniz gerekmektedir.

2. **Test Verileri**: Email adresleri ve kullanıcı bilgileri her testte değiştirilmelidir, aksi takdirde "Email zaten kayıtlı" hatası alabilirsiniz.

3. **Ekran Görüntüsü**: Test başarısız olduğunda otomatik olarak `registration_error.png` adında ekran görüntüsü alınır.

## İki Test Yaklaşımı

### 1. test_registration.py
- Basit ve doğrudan test yaklaşımı
- Hızlı prototipleme için uygundur

### 2. test_registration_pom.py
- Page Object Model (POM) design pattern kullanır
- Daha sürdürülebilir ve ölçeklenebilir
- Büyük projeler için önerilir
- Kod tekrarını azaltır

## Geliştirme Önerileri

1. Test verilerini harici bir dosyadan (JSON, Excel) okuyabilirsiniz
2. Farklı tarayıcılar için cross-browser testing ekleyebilirsiniz
3. Allure veya HTML rapor oluşturucuları ekleyebilirsiniz
4. CI/CD pipeline'a entegre edebilirsiniz (GitHub Actions, Jenkins, vb.)

## Sorun Giderme

- **ChromeDriver hatası**: `webdriver-manager` otomatik olarak driver'ı indirir, internet bağlantınızı kontrol edin
- **Element bulunamadı**: Locator'ları kontrol edin ve bekleme sürelerini artırın
- **Test çok hızlı**: `time.sleep()` değerlerini artırabilirsiniz

## Lisans

Bu proje test amaçlıdır.
