from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChatPage(BasePage):
    """Chat/Mesaj sayfası için Page Object"""


    #Mesaj içerikleri
    MESSAGE_TO_DOCTOR1  = "Başımın ön tarafında ve gözlerimde şiddetli bir ağrı var. Ne yapmalıyım?"
    MESSAGE_TO_DOCTOR2  = "Teşekkürler."
    
    # Locators
    DOCTOR_BUTTON = (By.XPATH, "//button[@data-code-name='Doktor']")  
    MESSAGE_INPUT = (By.XPATH, "//textarea[@placeholder='Mesajınızı buraya yazın...' or @name='message']")
    SEND_BUTTON = (By.XPATH, "//button[@id='send-btn' or contains(text(), 'Gönder')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_doctor_button(self):
        """Doktor butonuna tıkla"""
        self.click_element(self.DOCTOR_BUTTON)
    
    def enter_message(self, message):
        """Mesaj alanına yazı yaz"""
        self.input_text(self.MESSAGE_INPUT, message)
    
    def click_send_button(self):
        """Gönder butonuna tıkla"""
        self.click_element(self.SEND_BUTTON)
    
    def send_message_to_doctor(self, message):
        """Doktora mesaj gönder (tüm adımlar)"""
        self.click_doctor_button()
        self.enter_message(message)
        self.click_send_button()
