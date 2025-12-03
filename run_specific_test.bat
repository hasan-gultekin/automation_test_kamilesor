@echo off
REM Specific Test Execution - Belirli testleri calistirir

echo ========================================
echo Test Senaryosu Secimi
echo ========================================
echo 1. Kayit Testi (test_1_registration.py)
echo 2. Giris Testi (test_2_login.py)
echo 3. Doktor Chat Testi (test_3_doctor_chat.py)
echo 4. TUM TESTLER (Sirali)
echo ========================================
echo.

set /p choice="Seciminiz (1-4): "

if "%choice%"=="1" (
    echo.
    echo Kayit testi calistiriliyor...
    py -m pytest tests/test_1_registration.py -v -s --html=test-reports/registration-report.html --self-contained-html
) else if "%choice%"=="2" (
    echo.
    echo Giris testi calistiriliyor...
    py -m pytest tests/test_2_login.py -v -s --html=test-reports/login-report.html --self-contained-html
) else if "%choice%"=="3" (
    echo.
    echo Doktor chat testi calistiriliyor...
    py -m pytest tests/test_3_doctor_chat.py -v -s --html=test-reports/doctor-chat-report.html --self-contained-html
) else if "%choice%"=="4" (
    echo.
    echo Tum testler sirali calistiriliyor...
    py -m pytest tests/ -v -s --html=test-reports/all-tests-report.html --self-contained-html
) else (
    echo.
    echo Gecersiz secim!
    pause
    exit
)

echo.
echo ========================================
echo Test tamamlandi!
echo Rapor: test-reports\ klasorunde
echo ========================================
pause
