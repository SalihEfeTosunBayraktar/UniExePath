@echo off
echo ========================================
echo   UniExePath - Build Script
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt pyinstaller >nul 2>&1

echo Building UniExePath.exe...
python -m PyInstaller --onefile --noconsole --name "UniExePath" --add-binary "rcedit-x64.exe;." --hidden-import icoextract --hidden-import pefile builder.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo Moving EXE to root...
move /Y "dist\UniExePath.exe" "UniExePath.exe" >nul

echo Cleaning up build files...
rmdir /S /Q dist 2>nul
rmdir /S /Q build 2>nul
del /Q UniExePath.spec 2>nul

echo.
echo ========================================
echo   Build complete: UniExePath.exe
echo ========================================
pause
