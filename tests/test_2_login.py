import pytest
import sys
import os
import time

# Proje kök dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from utils.driver_helper import get_chrome_driver
from utils.test_data_helper import generate_test_user_data
import config


class TestLogin:
    """Giriş testleri - Düzenli proje yapısı ile"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Test başlamadan önce browser'ı başlat"""
        self.driver = get_chrome_driver()
        self.driver.implicitly_wait(config.IMPLICIT_WAIT)
        self.login_page = LoginPage(self.driver)
        yield
        # Test bittikten sonra browser'ı kapat
        self.driver.quit()
    
    def test_successful_login(self):
        """Başarılı kullanıcı kaydı testi"""
        # Ana sayfaya git
        self.driver.get(config.BASE_URL)
        print(f"\n✓ Ana sayfaya gidildi: {config.BASE_URL}")
        time.sleep(2)
        
        try:
            # Giriş yap linkine tıkla
            self.login_page.click_login_link()
            print("✓ Giriş sayfasına gidildi")
            time.sleep(2)
            
            # Giriş formunu doldur - Config'den bilgileri al
            self.login_page.fill_login_form(
                config.LOGIN_USER,
                config.LOGIN_PASSWORD
            )
            print(f"✓ Form dolduruldu (Email: {config.LOGIN_USER})")
            
            time.sleep(1)
            
            # Formu gönder
            self.login_page.submit_login()
            print("✓ Form gönderildi")
            
            time.sleep(5)
            
            # Başarılı kayıt doğrulaması
            assert self.login_page.is_login_successful(), \
                "Giriş sonrası sayfa değişmedi"
            
            current_url = self.login_page.get_current_url()
            print(f"✓ Giriş başarılı! Yönlendirilen URL: {current_url}")
            
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            self.driver.save_screenshot("tests/screenshots/login_error.png")
            print(f"❌ Test hatası: {str(e)}")
            raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
