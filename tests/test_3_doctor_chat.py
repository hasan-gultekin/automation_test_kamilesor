import pytest
import sys
import os
import time

# Proje kök dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.chat_page import ChatPage


class TestDoctorChat:
    """Doktor ile mesajlaşma testleri - Login precondition ile"""
    
    def test_send_message_to_doctor(self, logged_in_browser):
        """Doktora mesaj gönderme testi"""
        driver = logged_in_browser
        chat_page = ChatPage(driver)
        
        try:
            # Doktor butonuna tıkla
            chat_page.click_doctor_button()
            print("✓ Doktor butonuna tıklandı")
            time.sleep(2)
            
            # Mesaj yaz
            test_message = chat_page.MESSAGE_TO_DOCTOR1
            chat_page.enter_message(test_message)
            print(f"✓ Mesaj yazıldı: '{test_message}'")
            time.sleep(1)
            
            # Gönder butonuna tıkla
            chat_page.click_send_button()
            print("✓ Gönder butonuna tıklandı")
            time.sleep(15)
            
            print("✓ Mesaj gönderme işlemi tamamlandı!")
            
            
            # İkinci mesajı yaz
            test_message = chat_page.MESSAGE_TO_DOCTOR2
            chat_page.enter_message(test_message)
            print(f"✓ Mesaj yazıldı: '{test_message}'")
            time.sleep(1)

         # İkinci mesajı gönder
            chat_page.click_send_button()
            print("✓ Gönder butonuna tıklandı")
            time.sleep(1)
            
            print("✓ Mesaj gönderme işlemi tamamlandı!")
            
            
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            driver.save_screenshot("tests/screenshots/doctor_chat_error.png")
            print(f"❌ Test hatası: {str(e)}")
            raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
