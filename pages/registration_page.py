from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Kayıt sayfası için Page Object"""
    
    # Locators - Gerçek Kamile Sor site yapısı
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    SIGNUP_LINK = (By.XPATH, "//a[@href='/signup']")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SIGNUP_URL = "https://kamilesor.com/signup"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_login_link(self):
        """Giriş yap linkine tıkla"""
        self.click_element(self.LOGIN_LINK)
    
    def click_signup_link(self):
        """Kayıt ol linkine tıkla"""
        self.click_element(self.SIGNUP_LINK)
    
    def fill_registration_form(self, first_name, last_name, email, password):
        """Kayıt formunu doldur"""
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
    
    def submit_registration(self):
        """Kayıt formunu gönder"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def is_registration_successful(self):
        """Kayıt başarılı mı kontrol et (URL değişti mi?)"""
        return self.driver.current_url != self.SIGNUP_URL
    
    def get_current_url(self):
        """Mevcut URL'i al"""
        return self.driver.current_url
