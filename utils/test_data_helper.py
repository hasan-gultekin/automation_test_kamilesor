"""
Test Data Helper - Test verileri oluşturma fonksiyonları
"""
import random
import string


def generate_random_email(domain="example.com"):
    """
    Random email adresi üretir
    Args:
        domain (str): Email domain
    Returns:
        str: Random email adresi
    """
    random_num = random.randint(1000, 9999)
    random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"test{random_string}{random_num}@{domain}"


def generate_test_user_data():
    """
    Test kullanıcı verisi üretir
    Returns:
        dict: Kullanıcı bilgileri
    """
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": generate_random_email(),
        "password": "TestPassword123!"
    }
