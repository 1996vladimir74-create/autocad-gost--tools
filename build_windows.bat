@echo off


echo Building AutoCAD GOST Tools...


pip install -r requirements.txt


pyinstaller ^
AutoCAD_GOST_Tools.spec


echo.
echo Build completed.
echo File:
echo dist\AutoCAD_GOST_Tools.exe


pause
