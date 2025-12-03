"""
Pytest configuration and shared fixtures
"""
import pytest
import sys
import os
import time

# Proje kök dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).replace('tests', ''))

from pages.login_page import LoginPage
from utils.driver_helper import get_chrome_driver
import config


@pytest.fixture(scope="function")
def browser():
    """Browser fixture - Test boyunca açık kalır"""
    driver = get_chrome_driver()
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    yield driver
    # Test bittikten sonra browser'ı kapat
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_browser(browser):
    """
    Precondition: Kullanıcı giriş yapmış browser döndürür
    Login işlemini gerçekleştirir ve browser'ı açık tutar
    """
    driver = browser
    login_page = LoginPage(driver)
    
    print("\n" + "="*60)
    print("PRECONDITION: Login işlemi başlatılıyor...")
    print("="*60)
    
    # Ana sayfaya git
    driver.get(config.BASE_URL)
    print(f"✓ Ana sayfaya gidildi: {config.BASE_URL}")
    time.sleep(2)
    
    # Giriş yap linkine tıkla
    login_page.click_login_link()
    print("✓ Giriş sayfasına gidildi")
    time.sleep(2)
    
    # Giriş formunu doldur
    login_page.fill_login_form(
        config.LOGIN_USER,
        config.LOGIN_PASSWORD
    )
    print(f"✓ Form dolduruldu (Email: {config.LOGIN_USER})")
    time.sleep(1)
    
    # Formu gönder
    login_page.submit_login()
    print("✓ Form gönderildi")
    time.sleep(5)
    
    # Başarılı giriş doğrulaması
    assert login_page.is_login_successful(), "Giriş başarısız!"
    
    current_url = login_page.get_current_url()
    print(f"✓ Giriş başarılı! URL: {current_url}")
    print("="*60)
    print("PRECONDITION TAMAMLANDI - Test senaryosu başlıyor...")
    print("="*60 + "\n")
    
    yield driver
    # Browser'ı kapatma, bu browser fixture'ı yapacak
