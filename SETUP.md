# TF-Alerter Development Setup

## Prerequisites

- **Python 3.10+** (tested with Python 3.14)
- **Windows** (primary platform)

## Installation

### Option 1: Automatic Installation (Windows)

Simply run the batch script:

```batch
install_dependencies.bat
```

### Option 2: Manual Installation

1. **Install Python** from https://www.python.org/

2. **Open Terminal/Command Prompt** in the project directory

3. **Upgrade pip:**
```bash
python -m pip install --upgrade pip
```

4. **Install all dependencies:**
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install PyQt6==6.10.2
pip install pynput==1.7.6
pip install pygame
pip install qrcode==8.2
pip install pillow==12.1.0
pip install pyttsx3==2.90
pip install edge-tts==7.2.7
pip install requests==2.32.3
pip install psutil
```

## Running the Application

```bash
python main.py
```

## Troubleshooting

### Import Errors in VS Code

If VS Code shows import errors even after installation:

1. **Restart VS Code** (Ctrl+Shift+P → Developer: Reload Window)
2. **Check Python Interpreter** is correctly selected
3. **Verify Installation:**
   ```bash
   python -c "import pyttsx3; import edge_tts; import PyQt6; print('All modules OK!')"
   ```

### pygame Build Errors

If pygame fails to compile, use the pre-built wheel:

```bash
pip install pygame --only-binary :all:
```

### Edge TTS Issues

For Edge TTS to work, you need:
- Active internet connection
- Windows 10+ or compatible OS

For offline TTS, use the System TTS option (pyttsx3) in settings.

### Missing Sounds

Ensure the following directories exist in the project root:
```
Sounds/
  ├── Tick/
  ├── Transition/
  └── Voice/
Logo/
  └── Logo.png
```

## Module Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| PyQt6 | 6.10.2 | GUI Framework |
| PyQt6-Multimedia | auto | Audio playback |
| pynput | 1.7.6 | Global hotkeys |
| pygame | latest | Audio processing |
| qrcode | 8.2 | QR code generation |
| Pillow | 12.1.0 | Image processing |
| pyttsx3 | 2.90 | System TTS (offline) |
| edge-tts | 7.2.7 | Microsoft Edge TTS (online) |
| requests | 2.32.3 | HTTP API calls for exchanges |
| psutil | latest | System monitoring |

## First Run Setup

When you first run the application:

1. A settings file will be created at: `AppData/Roaming/MyTradeTools/TF-Alerter`
2. Configure your preferences in the Settings dialog
3. Select exchanges for funding monitoring
4. Test the overlay with a hotkey

## Exchange Integration

The application connects to these exchanges via API:

- **Binance** - `https://fapi.binance.com/fapi/v1/fundingRate`
- **Bybit** - `https://api.bybit.com/v5/market/tickers`
- **OKX** - `https://www.okx.com/api/v5/market/funding-rate`
- **Gate.io** - `https://api.gateio.ws/api/v4/futures/usdt/funding_rates`
- **Bitget** - `https://api.bitget.com/api/v2/mix/market/current-fund-rate`

No authentication required for public endpoints.

### Development

### Quick Validation

```bash
python -m py_compile main.py funding_alerts.py listing_alerts.py
```

### Check Python Syntax

```bash
python -m py_compile main.py
```

### List All Imports

```bash
python -c "import sys; import main" 2>&1 | grep "^ModuleNotFoundError"
```
