# Project File Structure

## Essential Files (Required to Run)

### Application Entry Points
- `main.py` - Main application entry point
- `gui.py` - GUI components and layouts
- `logic.py` - Business logic and market data
- `overlay.py` - Chart overlay rendering

### Configuration & Data
- `config.py` - Application configuration constants
- `requirements.txt` - Python dependencies list
- `.gitignore` - Git ignore patterns

### Dialogs & UI Components
- `about_dialog.py` - About dialog
- `settings_dialog.py` - Settings configuration dialog
- `color_picker_dialog.py` - Color selection dialog
- `font_picker_dialog.py` - Font selection dialog
- `donate_dialog.py` - Donation information dialog

### Features
- `hotkey_manager.py` - Global hotkey handling
- `funding_alerts.py` - Cryptocurrency funding rate monitor

### Utilities
- `launcher.py` - Application launcher utility
- `clear_settings.py` - Settings cleanup utility

## Resources (Required)

### Directories
```
Logo/
  └── Logo.png              - Application icon

Sounds/
  ├── Tick/                 - Tick sound effects
  ├── Transition/           - Transition sound files
  └── Voice/                - Voice alert files
      └── README.txt
```

### Optional
```
Other_Sounds/              - Alternative sound resources
__pycache__/               - Python cache (auto-generated, can delete)
```

## Installation & Setup Files

- `install_dependencies.bat` - Automatic dependency installer (Windows)
- `run.bat` - Quick launcher for the application
- `SETUP.md` - Detailed setup instructions
- `INSTALLATION_SUCCESS.txt` - Post-installation information
- `FILE_STRUCTURE.md` - This file

## Testing

- Standalone legacy test scripts were removed from the repository.
- For validation, run syntax/import checks and launch `main.py`.

## .gitignore Rules

```
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.pytest_cache/
settings.ini
debug.log
```

## Dependencies Summary

| Module | Purpose | Installation |
|--------|---------|--------------|
| PyQt6 | GUI Framework | pip install PyQt6==6.10.2 |
| pynput | Hotkey Detection | pip install pynput==1.7.6 |
| qrcode | QR Generation | pip install qrcode==8.2 |
| Pillow | Image Processing | pip install pillow==12.1.0 |
| pyttsx3 | System TTS | pip install pyttsx3==2.90 |
| edge-tts | Online TTS | pip install edge-tts==7.2.7 |
| requests | HTTP Requests | pip install requests==2.32.3 |
| psutil | System Monitoring | pip install psutil |

## Quick Setup Checklist

- [ ] Python 3.10+ installed
- [ ] Clone/Download project
- [ ] Run: `install_dependencies.bat`
- [ ] Run: `python main.py` or `run.bat`
- [ ] Configure in Settings dialog
- [ ] Enable Funding tab
- [ ] Test hotkeys

## Python Entry Points

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Run application
python main.py

# Quick validation
python -m py_compile main.py funding_alerts.py listing_alerts.py

# Verify installation
python -c "import PyQt6; import pyttsx3; print('OK')"
```

## File Sizes Reference

- main.py: ~2,300 lines
- gui.py: GUI components
- logic.py: Market data & processing
- overlay.py: Chart overlay system
- funding_alerts.py: Exchange monitoring

Total: ~10,000+ lines of Python code

## Last Updated

February 17, 2026

## Support

For issues:
1. Check SETUP.md for common problems
2. Verify all dependencies: `pip list`
3. Run quick validation: `python -m py_compile main.py funding_alerts.py listing_alerts.py`
4. Check event logs or terminal output for errors
