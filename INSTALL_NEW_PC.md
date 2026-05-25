# Installation Guide for New PC

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Python
1. Download Python 3.10+ from https://www.python.org/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation in Command Prompt:
   ```
   python --version
   ```

### Step 2: Install Dependencies
Navigate to the project folder and run:

**Windows (Automatic):**
```batch
install_dependencies.bat
```

**Or Manual (all platforms):**
```bash
pip install -r requirements.txt
```

### Step 3: Run Application
```batch
python main.py
```
Or simply double-click: `run.bat`

---

## ⚙️ Detailed Setup Instructions

### 1. Python Installation (Windows)

1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.14" (or latest 3.10+)
3. Run the installer
4. **✓ CHECK: "Add Python to PATH"** ← IMPORTANT!
5. Click "Install Now"
6. Wait for installation to complete
7. Open Command Prompt and verify:
   ```
   python --version
   ```
   Should show: `Python 3.14.x` or similar

### 2. Install Dependencies

Option A - **Automatic (recommended for Windows):**
1. Extract project to a folder
2. Double-click: `install_dependencies.bat`
3. Wait for completion message
4. Press Enter to close

Option B - **Manual Command Line:**
1. Open Command Prompt in project folder
2. Run:
   ```bash
   pip install -r requirements.txt
   ```
3. Wait for all packages to install

### 3. First Launch

**Method 1 - Quick Launch (Windows):**
- Double-click: `run.bat`

**Method 2 - Command Line:**
```bash
python main.py
```

---

## ✅ Verification Checklist

### After Installation

1. **Check Python:**
   ```bash
   python --version
   ```
   ✓ Should show Python 3.10+

2. **Check pip:**
   ```bash
   pip --version
   ```
   ✓ Should show version number

3. **Check Dependencies:**
   ```bash
   pip list
   ```
   ✓ Should show: PyQt6, pyttsx3, edge-tts, requests, etc.

4. **Check Imports:**
   ```bash
   python -c "import PyQt6; import pyttsx3; print('OK')"
   ```
   ✓ Should output: `OK`

5. **Quick Run Check:**
   ```bash
   python -m py_compile main.py funding_alerts.py listing_alerts.py
   python main.py
   ```
   ✓ App should start without import/syntax errors

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"
**Solution:**
1. Make sure you installed Python with "Add to PATH" checked
2. Close and reopen Command Prompt
3. If still failing, reinstall Python with PATH option

### Problem: "ModuleNotFoundError" when running
**Solution:**
```bash
pip install -r requirements.txt
```
If that fails, try:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt --upgrade
```

### Problem: "Edge TTS not available" warning
**Solution:**
- This is normal and not critical
- App will use system TTS (pyttsx3) instead
- Both work without internet for offline TTS

### Problem: Font errors in console
**Solution:**
- These are harmless warnings from PyQt6
- Application will still work fine

### Problem: Application won't start
**Solution:**
1. Close all instances of the app
2. Delete `__pycache__` folder
3. Run again: `python main.py`

### Problem: Can't click checkboxes / UI not responsive
**Solution:**
1. Make sure you're using latest PyQt6:
   ```bash
   pip install --upgrade PyQt6
   ```
2. If still failing, try reinstalling:
   ```bash
   pip install --force-reinstall PyQt6
   ```

---

## 📦 What Gets Installed

The following packages will be installed automatically:

| Package | Size | Purpose |
|---------|------|---------|
| PyQt6 | ~10MB | GUI framework |
| pyttsx3 | ~1MB | System text-to-speech |
| edge-tts | ~5MB | Online text-to-speech |
| requests | ~1MB | HTTP API client |
| pynput | ~1MB | Global hotkeys |
| qrcode | ~1MB | QR code generation |
| pillow | ~10MB | Image processing |
| psutil | ~5MB | System monitoring |

**Total: ~35MB** (with Python packages)

---

## 🎯 First Run Setup

After starting the application:

1. **Settings Tab:**
   - Select TTS engine (System or Edge)
   - Choose voice language (Russian/English)
   - Set volume levels

2. **Funding Tab:**
   - ✓ Check "Gate", "Bybit", "Binance" boxes
   - Set "Minutes to Funding" threshold
   - Configure sound and voice alerts

3. **Hotkeys:**
   - Set your preferred hotkey for overlay toggle
   - Test the hotkey

4. **Start Trading:**
   - Navigate to the exchange
   - Use overlay with hotkey
   - Monitor funding rates

---

## 📞 Support

If you encounter issues:

1. **Check the logs:**
   - Look at command prompt output for error messages
   - Check for `debug.log` file in project folder

2. **Run diagnostics:**
   ```bash
   python -c "import sys; print(sys.executable)"
   ```
   This shows which Python is being used

3. **Common solutions:**
   - Update pip: `python -m pip install --upgrade pip`
   - Reinstall all: `pip install -r requirements.txt --upgrade`
   - Delete cache: Remove `__pycache__` folder

---

## 📝 Advanced Setup (Optional)

### Using Virtual Environment (Recommended for Development)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate.bat
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Running in Background (Advanced)

```bash
# Start in background (Windows)
start python main.py

# Or use task scheduler to run at startup
```

---

## ✨ Tips

1. **Keep it Updated:**
   - Periodically run: `pip install -r requirements.txt --upgrade`

2. **Backup Settings:**
   - Settings are saved in Windows Registry
   - Path: `HKEY_CURRENT_USER\Software\MyTradeTools\TF-Alerter`

3. **Performance Tips:**
   - Close other applications if overlay is slow
   - Reduce chart refresh rate in settings
   - Disable notifications if CPU is high

4. **Internet:**
   - App works offline for most features
   - Only needs internet for Edge TTS and exchange APIs

---

## 📅 Version Information

- **Python Required:** 3.10+
- **Last Tested:** Python 3.14
- **Platform:** Windows (primary)
- **Last Updated:** February 2026

---

Good luck! 🚀
