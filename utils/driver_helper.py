"""
Driver Helper - WebDriver yönetimi için yardımcı fonksiyonlar
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def get_chrome_driver():
    """
    Chrome WebDriver'ı başlatır
    Returns:
        WebDriver: Yapılandırılmış Chrome WebDriver instance
    """
    # ChromeDriver yolu
    chrome_driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chromedriver.exe")
    
    try:
        # Manuel yol ile çalıştır
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
    except:
        # PATH'ten dene
        driver = webdriver.Chrome()
    
    driver.maximize_window()
    return driver
