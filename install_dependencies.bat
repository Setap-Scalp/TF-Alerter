@echo off
REM ============================================
REM Installation script for TF-Alerter
REM ============================================

echo.
echo === TF-Alerter Dependencies Installation ===
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [*] Python found:
python --version
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install all dependencies
echo [*] Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)

echo.
echo === Installation Complete! ===
echo.
echo You can now run the application:
echo   python main.py
echo.
pause
