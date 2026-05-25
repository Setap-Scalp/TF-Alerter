@echo off
REM ============================================
REM Launch script for TF-Alerter
REM ============================================

echo.
echo === TF-Alerter Launcher ===
echo.

cd /d "%~dp0"

set "PY_EXE="
if exist ".venv\Scripts\python.exe" set "PY_EXE=.venv\Scripts\python.exe"
if not defined PY_EXE if exist ".venv-1\Scripts\python.exe" set "PY_EXE=.venv-1\Scripts\python.exe"

if not defined PY_EXE (
    echo ERROR: Virtual environment not found.
    echo Expected one of:
    echo   .venv\Scripts\python.exe
    echo   .venv-1\Scripts\python.exe
    echo.
    echo Create/install environment first, for example:
    echo   uv venv .venv
    echo   uv pip install --python .venv\Scripts\python.exe -r requirements.txt
    pause
    exit /b 1
)

echo [*] Starting TF-Alerter...
echo [*] Python: %PY_EXE%
echo.

"%PY_EXE%" main.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start application
    echo Make sure dependencies are installed in the selected venv.
    pause
    exit /b 1
)
