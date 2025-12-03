"""
Login sayfasını ve kayıt formunu incele
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ChromeDriver yolu
chrome_driver_path = r"c:\seleniumPython\kamile_sor_test\chromedriver.exe"

# Browser'ı başlat
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Login sayfasına git
    print("Login sayfasına gidiliyor...")
    driver.get("https://kamilesor.com/login")
    time.sleep(3)
    
    # Sayfa başlığı
    print(f"\n=== SAYFA BAŞLIĞI ===")
    print(f"Title: {driver.title}")
    print(f"URL: {driver.current_url}")
    
    # Sayfadaki tüm linkleri bul
    print(f"\n=== SAYFADAKI TÜM LİNKLER ===")
    links = driver.find_elements(By.TAG_NAME, "a")
    for i, link in enumerate(links):
        text = link.text.strip()
        href = link.get_attribute("href")
        class_name = link.get_attribute("class")
        if text or href:
            print(f"{i+1}. Text: '{text}' | Href: {href} | Class: {class_name}")
    
    # Butonları bul
    print(f"\n=== SAYFADAKI BUTONLAR ===")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for i, btn in enumerate(buttons):
        print(f"{i+1}. Text: '{btn.text}' | Type: {btn.get_attribute('type')} | Class: {btn.get_attribute('class')} | ID: {btn.get_attribute('id')}")
    
    # Formları bul
    print(f"\n=== SAYFADAKI FORMLAR ===")
    forms = driver.find_elements(By.TAG_NAME, "form")
    print(f"Toplam {len(forms)} form bulundu")
    for i, form in enumerate(forms):
        print(f"\nForm {i+1}:")
        print(f"  - Action: {form.get_attribute('action')}")
        print(f"  - Method: {form.get_attribute('method')}")
        print(f"  - Class: {form.get_attribute('class')}")
        print(f"  - ID: {form.get_attribute('id')}")
        
        # Form içindeki tüm elementleri listele
        inputs = form.find_elements(By.TAG_NAME, "input")
        if inputs:
            print(f"  - Inputs ({len(inputs)}):")
            for inp in inputs:
                print(f"    * Type: {inp.get_attribute('type')} | Name: {inp.get_attribute('name')} | ID: {inp.get_attribute('id')} | Placeholder: {inp.get_attribute('placeholder')} | Class: {inp.get_attribute('class')}")
    
    # Kayıt ile ilgili elementleri ara
    print(f"\n=== 'KAYIT', 'REGISTER', 'SIGN UP' İÇEREN ELEMENTLER ===")
    keywords = ["kayıt", "kayit", "üye ol", "uye ol", "register", "sign up", "signup", "create account"]
    
    for keyword in keywords:
        try:
            # Tüm elementlerde ara
            elements = driver.find_elements(By.XPATH, f"//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZĞÜŞÖÇI', 'abcdefghijklmnopqrstuvwxyzğüşöçı'), '{keyword.lower()}')]")
            if elements:
                print(f"\n'{keyword}' içeren elementler ({len(elements)}):")
                for elem in elements[:5]:  # İlk 5'i göster
                    tag = elem.tag_name
                    text = elem.text[:50] if elem.text else ""
                    print(f"  - Tag: <{tag}> | Text: '{text}' | Class: {elem.get_attribute('class')} | ID: {elem.get_attribute('id')}")
        except:
            pass
    
    # Ekran görüntüsü al
    driver.save_screenshot("login_page_screenshot.png")
    print(f"\n✓ Ekran görüntüsü kaydedildi: login_page_screenshot.png")
    
    # Sayfanın HTML'ini kaydet
    with open("login_page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"✓ Sayfa kaynağı kaydedildi: login_page_source.html")
    
    print("\n" + "="*60)
    print("Tarayıcı 30 saniye açık kalacak.")
    print("Manuel olarak kayıt sayfasını bulup F12 ile inceleyebilirsiniz.")
    print("="*60)
    time.sleep(30)
    
except Exception as e:
    print(f"\nHata: {e}")
    import traceback
    traceback.print_exc()
    driver.save_screenshot("error_screenshot.png")
    
finally:
    print("\nTarayıcı kapatılıyor...")
    driver.quit()
    print("Bitti!")
