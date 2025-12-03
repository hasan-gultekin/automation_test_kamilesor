from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Kayıt sayfası için Page Object"""
    
    # Locators - Gerçek Kamile Sor site yapısı
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_URL = "https://kamilesor.com/login"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_login_link(self):
        """Giriş yap linkine tıkla"""
        self.click_element(self.LOGIN_LINK)
    
    
    def fill_login_form(self, email, password):
        """Giriş formunu doldur"""
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
    
    def submit_login(self):
        """Giriş formunu gönder"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def is_login_successful(self):
        """Giriş başarılı mı kontrol et (URL değişti mi?)"""
        return self.driver.current_url != self.LOGIN_URL
    
    def get_current_url(self):
        """Mevcut URL'i al"""
        return self.driver.current_url
