# Kamile Sor Test Otomasyonu

Bu proje, https://kamilesor.com sitesinde kayıt olma işlemini test etmek için Selenium ve Python kullanılarak oluşturulmuş bir test otomasyon projesidir.

## Proje Yapısı

```
automation_test_kamilesor/
├── pages/                          # Page Object Model dosyaları
│   ├── __init__.py
│   ├── base_page.py               # Temel sayfa sınıfı
│   ├── registration_page.py       # Kayıt sayfası
│   ├── login_page.py              # Login sayfası
│   └── chat_page.py               # Chat sayfası
├── tests/                          # Test dosyaları
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixture'ları
│   ├── test_1_registration.py     # Kayıt testleri
│   ├── test_2_login.py            # Login testleri
│   ├── test_3_doctor_chat.py      # Chat testleri
│   └── screenshots/               # Test ekran görüntüleri
├── utils/                          # Yardımcı araçlar
│   ├── __init__.py
│   ├── driver_helper.py           # WebDriver yönetimi
│   └── test_data_helper.py        # Test verisi oluşturma
├── test-reports/                   # HTML test raporları
├── config.py                       # Yapılandırma dosyası
├── config.example.py              # Örnek yapılandırma
├── requirements.txt                # Python bağımlılıkları
├── pytest.ini                      # Pytest yapılandırması
├── run_tests.bat                   # Tüm testleri çalıştırma (Windows)
├── run_specific_test.bat          # Belirli test çalıştırma (Windows)
└── README.md                       # Proje dokümantasyonu
```

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- Google Chrome tarayıcı
- ChromeDriver (otomatik olarak indirilir)

## 🔧 Kurulum

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/hasan-gultekin/automation_test_kamilesor.git
cd automation_test_kamilesor
```

### 2. Sanal Ortam Oluşturun (Önerilen)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# veya
source venv/bin/activate  # Linux/Mac
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Yapılandırma Dosyasını Ayarlayın

`config.example.py` dosyasını `config.py` olarak kopyalayın ve gerekli ayarları yapın:

```bash
copy config.example.py config.py  # Windows
# veya
cp config.example.py config.py    # Linux/Mac
```

## 🎯 Testleri Çalıştırma

### Windows'ta Otomatik Çalıştırma

**Tüm testleri çalıştır:**
```bash
run_tests.bat
```

**Belirli bir testi çalıştır:**
```bash
run_specific_test.bat
```

### Manuel Çalıştırma

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

Bu proje test ve eğitim amaçlı geliştirilmiştir.

## 📧 İletişim

Hasan Gültekin - [@hasan-gultekin](https://github.com/hasan-gultekin)

Proje Linki: [https://github.com/hasan-gultekin/automation_test_kamilesor](https://github.com/hasan-gultekin/automation_test_kamilesor)
