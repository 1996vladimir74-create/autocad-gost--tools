@echo off
setlocal
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m PyInstaller --onefile --windowed --name AutoCAD_GOST_Tools main.py
if errorlevel 1 (
    echo Build failed.
    exit /b 1
)
echo.
echo EXE created at dist\AutoCAD_GOST_Tools.exe
