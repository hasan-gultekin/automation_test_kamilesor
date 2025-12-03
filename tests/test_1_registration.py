import pytest
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
import time

# Proje kök dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.registration_page import RegistrationPage
from utils.driver_helper import get_chrome_driver
from utils.test_data_helper import generate_test_user_data
import config


class TestRegistration:
    """Kayıt testleri - Düzenli proje yapısı ile"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Test başlamadan önce browser'ı başlat"""
        self.driver = get_chrome_driver()
        self.driver.implicitly_wait(config.IMPLICIT_WAIT)
        self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)
        self.registration_page = RegistrationPage(self.driver)
        yield
        # Test bittikten sonra browser'ı kapat
        self.driver.quit()
    
    def test_successful_registration(self):
        """Başarılı kullanıcı kaydı testi"""
        # Ana sayfaya git
        self.driver.get(config.BASE_URL)
        print(f"\n✓ Ana sayfaya gidildi: {config.BASE_URL}")
        time.sleep(2)
        
        try:
            # Giriş yap linkine tıkla
            self.registration_page.click_login_link()
            print("✓ Giriş sayfasına gidildi")
            time.sleep(2)
            
            # Kayıt ol linkine tıkla
            self.registration_page.click_signup_link()
            print("✓ Kayıt sayfasına gidildi")
            time.sleep(2)
            
            # Test verilerini oluştur
            test_data = generate_test_user_data()
            
            # Kayıt formunu doldur
            self.registration_page.fill_registration_form(
                test_data["first_name"],
                test_data["last_name"],
                test_data["email"],
                test_data["password"]
            )
            print(f"✓ Form dolduruldu (Email: {test_data['email']})")
            
            time.sleep(1)
            
            # Formu gönder
            self.registration_page.submit_registration()
            print("✓ Form gönderildi")
            
            time.sleep(5)
            
            # Başarılı kayıt doğrulaması
            assert self.registration_page.is_registration_successful(), \
                "Kayıt sonrası sayfa değişmedi"
            
            current_url = self.registration_page.get_current_url()
            print(f"✓ Kayıt başarılı! Yönlendirilen URL: {current_url}")
            
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            self.driver.save_screenshot("tests/screenshots/registration_error.png")
            print(f"❌ Test hatası: {str(e)}")
            raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
