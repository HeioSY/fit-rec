@echo off
cd /d "%~dp0"

REM Sanal ortamı aktifleştir (venv klasörü Src'nin bir üstünde)
call ..\venv\Scripts\activate

REM Streamlit uygulamasını çalıştır
streamlit run app.py

pause
