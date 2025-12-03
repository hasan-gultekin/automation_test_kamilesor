# Kamile Sor Test Otomasyonu

Bu proje, https://kamilesor.com web sitesi için Selenium ve Python kullanılarak geliştirilmiş kapsamlı bir test otomasyon framework'üdür. Page Object Model (POM) tasarım deseni kullanılarak yapılandırılmıştır.

## 🚀 Özellikler

- ✅ **Kullanıcı Kaydı Testleri** - Yeni kullanıcı kaydı senaryolarını test eder
- ✅ **Login Testleri** - Kullanıcı girişi ve doğrulama testleri
- ✅ **Doktor Chat Testleri** - Chat fonksiyonellik testleri
- ✅ **Page Object Model (POM)** - Sürdürülebilir ve ölçeklenebilir test yapısı
- ✅ **HTML Test Raporları** - pytest-html ile detaylı test raporları
- ✅ **Screenshot Yönetimi** - Hata durumlarında otomatik ekran görüntüsü
- ✅ **Dinamik Test Verileri** - Her test için benzersiz veriler

## 📁 Proje Yapısı

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
pytest tests/ -v -s --html=test-reports/test-report.html --self-contained-html
```

**Sadece kayıt testlerini çalıştır:**
```bash
pytest tests/test_1_registration.py -v -s
```

**Sadece login testlerini çalıştır:**
```bash
pytest tests/test_2_login.py -v -s
```

**Sadece chat testlerini çalıştır:**
```bash
pytest tests/test_3_doctor_chat.py -v -s
```

## 📊 Test Raporları

Test çalıştırıldıktan sonra HTML raporu `test-reports/test-report.html` dosyasında oluşturulur. Bu rapor şunları içerir:

- Test sonuçları (Pass/Fail)
- Test süresi
- Hata mesajları
- Screenshot'lar (başarısız testler için)

## 🏗️ Page Object Model (POM)

Proje, Page Object Model tasarım desenini kullanır:

- **base_page.py**: Tüm sayfa sınıflarının miras aldığı temel sınıf
- **registration_page.py**: Kayıt sayfası işlemleri
- **login_page.py**: Giriş sayfası işlemleri
- **chat_page.py**: Chat sayfası işlemleri

### Örnek Kullanım

```python
from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("user@example.com", "password123")
    assert login_page.is_login_successful()
```

## 🛠️ Yapılandırma

`config.py` dosyasında aşağıdaki ayarları değiştirebilirsiniz:

```python
BASE_URL = "https://kamilesor.com"
BROWSER = "chrome"              # chrome, firefox, edge
IMPLICIT_WAIT = 10              # Saniye
EXPLICIT_WAIT = 20              # Saniye
HEADLESS = False                # True: Tarayıcı görünmeden çalışır
SCREENSHOT_ON_FAILURE = True    # Hata durumunda screenshot al
```

## 🔍 Test Verileri

Test verileri dinamik olarak `utils/test_data_helper.py` kullanılarak oluşturulur:

- Benzersiz email adresleri
- Rastgele kullanıcı adları
- Güvenli şifreler
- Telefon numaraları

## 📝 Test Senaryoları

### 1. Kayıt Testleri (`test_1_registration.py`)
- Yeni kullanıcı kaydı
- Form validasyonu
- Başarılı kayıt doğrulama

### 2. Login Testleri (`test_2_login.py`)
- Geçerli kimlik bilgileriyle giriş
- Geçersiz kimlik bilgileriyle giriş
- Şifre hatırlatma

### 3. Chat Testleri (`test_3_doctor_chat.py`)
- Doktor ile chat başlatma
- Mesaj gönderme
- Chat geçmişi kontrolü

## 🐛 Sorun Giderme

### ChromeDriver Hatası
```
webdriver-manager otomatik olarak driver'ı indirir.
İnternet bağlantınızı kontrol edin.
```

### Element Bulunamadı
```
- Locator'ları kontrol edin
- Bekleme sürelerini artırın (config.py)
- Sayfanın tamamen yüklendiğinden emin olun
```

### Import Hataları
```bash
# Python path'ini kontrol edin
set PYTHONPATH=%PYTHONPATH%;%CD%  # Windows
export PYTHONPATH=$PYTHONPATH:$(pwd)  # Linux/Mac
```

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje test ve eğitim amaçlı geliştirilmiştir.

## 📧 İletişim

Hasan Gültekin - [@hasan-gultekin](https://github.com/hasan-gultekin)

Proje Linki: [https://github.com/hasan-gultekin/automation_test_kamilesor](https://github.com/hasan-gultekin/automation_test_kamilesor)
