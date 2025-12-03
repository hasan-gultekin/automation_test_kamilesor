"""
Signup (Kayıt) sayfasını incele
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
    # Signup sayfasına git
    print("Signup sayfasına gidiliyor...")
    driver.get("https://kamilesor.com/signup")
    time.sleep(3)
    
    # Sayfa başlığı
    print(f"\n=== SAYFA BAŞLIĞI ===")
    print(f"Title: {driver.title}")
    print(f"URL: {driver.current_url}")
    
    # Formları bul
    print(f"\n=== KAYIT FORMU DETAYLARI ===")
    forms = driver.find_elements(By.TAG_NAME, "form")
    print(f"Toplam {len(forms)} form bulundu")
    
    for i, form in enumerate(forms):
        print(f"\nForm {i+1}:")
        print(f"  - Action: {form.get_attribute('action')}")
        print(f"  - Method: {form.get_attribute('method')}")
        print(f"  - Class: {form.get_attribute('class')}")
        print(f"  - ID: {form.get_attribute('id')}")
        
        # Form içindeki tüm INPUT elementleri
        inputs = form.find_elements(By.TAG_NAME, "input")
        if inputs:
            print(f"\n  INPUT ALANLARI ({len(inputs)}):")
            for j, inp in enumerate(inputs):
                inp_type = inp.get_attribute('type')
                inp_name = inp.get_attribute('name')
                inp_id = inp.get_attribute('id')
                inp_placeholder = inp.get_attribute('placeholder')
                inp_class = inp.get_attribute('class')
                inp_required = inp.get_attribute('required')
                print(f"    {j+1}. Type: {inp_type} | Name: '{inp_name}' | ID: '{inp_id}' | Placeholder: '{inp_placeholder}'")
                print(f"       Class: '{inp_class}' | Required: {inp_required}")
        
        # Textarea varsa
        textareas = form.find_elements(By.TAG_NAME, "textarea")
        if textareas:
            print(f"\n  TEXTAREA ALANLARI ({len(textareas)}):")
            for j, ta in enumerate(textareas):
                print(f"    {j+1}. Name: {ta.get_attribute('name')} | ID: {ta.get_attribute('id')} | Placeholder: {ta.get_attribute('placeholder')}")
        
        # Select varsa
        selects = form.find_elements(By.TAG_NAME, "select")
        if selects:
            print(f"\n  SELECT ALANLARI ({len(selects)}):")
            for j, sel in enumerate(selects):
                print(f"    {j+1}. Name: {sel.get_attribute('name')} | ID: {sel.get_attribute('id')}")
        
        # Butonlar
        buttons = form.find_elements(By.TAG_NAME, "button")
        if buttons:
            print(f"\n  BUTONLAR ({len(buttons)}):")
            for j, btn in enumerate(buttons):
                print(f"    {j+1}. Text: '{btn.text}' | Type: {btn.get_attribute('type')} | Class: '{btn.get_attribute('class')}' | ID: '{btn.get_attribute('id')}'")
    
    # Checkbox ve radio button'ları ara
    print(f"\n=== CHECKBOX VE RADIO BUTONLARI ===")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    if checkboxes:
        print(f"Checkbox'lar ({len(checkboxes)}):")
        for cb in checkboxes:
            print(f"  - Name: {cb.get_attribute('name')} | ID: {cb.get_attribute('id')} | Value: {cb.get_attribute('value')}")
            # Label'ı bul
            try:
                label = driver.find_element(By.XPATH, f"//label[@for='{cb.get_attribute('id')}']")
                print(f"    Label: '{label.text}'")
            except:
                pass
    
    radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
    if radios:
        print(f"Radio button'lar ({len(radios)}):")
        for rb in radios:
            print(f"  - Name: {rb.get_attribute('name')} | ID: {rb.get_attribute('id')} | Value: {rb.get_attribute('value')}")
    
    # Tüm label'ları listele
    print(f"\n=== LABEL'LAR ===")
    labels = driver.find_elements(By.TAG_NAME, "label")
    if labels:
        for i, label in enumerate(labels):
            label_for = label.get_attribute('for')
            label_text = label.text.strip()
            if label_text:
                print(f"{i+1}. Text: '{label_text}' | For: '{label_for}'")
    
    # Ekran görüntüsü al
    driver.save_screenshot("signup_page_screenshot.png")
    print(f"\n✓ Ekran görüntüsü kaydedildi: signup_page_screenshot.png")
    
    # Sayfanın HTML'ini kaydet
    with open("signup_page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"✓ Sayfa kaynağı kaydedildi: signup_page_source.html")
    
    print("\n" + "="*60)
    print("Tarayıcı 30 saniye açık kalacak.")
    print("Developer Tools (F12) ile elementleri inceleyebilirsiniz.")
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
