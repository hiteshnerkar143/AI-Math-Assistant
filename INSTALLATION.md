# Installation Guide - AI Math Assistant

## Prerequisites

Before installing the AI Math Assistant, ensure you have:
- **Python 3.8 or higher** installed
- **pip** (Python package manager) available
- **Internet connection** for downloading dependencies
- **At least 500MB** of free disk space

## Installation Steps

### Step 1: Verify Python Installation

Open your terminal/command prompt and verify Python is installed:

```bash
python --version
```

You should see version 3.8 or higher. If not, download from https://www.python.org/

### Step 2: Navigate to Project Directory

```bash
cd AI_Math_Assistant
```

### Step 3: Create Virtual Environment (Recommended)

Creating a virtual environment keeps project dependencies isolated:

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**Note**: You should see `(venv)` prefix in your terminal indicating the virtual environment is active.

### Step 4: Upgrade pip

Ensure you have the latest pip version:

```bash
python -m pip install --upgrade pip
```

### Step 5: Install Requirements

Install all project dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

This will install:
- **GUI Framework**: customtkinter, Pillow
- **Machine Learning**: scikit-learn, numpy
- **Mathematics**: sympy, scipy
- **Plotting**: matplotlib
- **PDF Generation**: reportlab
- **Voice Features**: SpeechRecognition, pyttsx3
- **Data Processing**: pandas

**Installation time**: Typically 3-5 minutes depending on internet speed

### Step 6: Verify Installation

Verify all packages installed correctly:

```bash
python -c "import customtkinter; import sklearn; import sympy; import matplotlib; print('✓ All packages installed successfully!')"
```

### Step 7: Run Application

Start the application:

```bash
python main.py
```

The GUI window should open with the "AI Math Assistant" title.

## Troubleshooting

### Issue: Module not found errors

**Solution**: Ensure virtual environment is activated and requirements.txt is installed:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: "customtkinter not found" on Linux

**Solution**: Install tkinter system package first:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (using Homebrew)
brew install python-tk
```

### Issue: Speech Recognition not working

**Solution**: Install additional audio libraries:
```bash
# Windows: Usually works out of the box

# macOS
brew install portaudio
pip install --upgrade SpeechRecognition

# Linux
sudo apt-get install portaudio19-dev
pip install --upgrade SpeechRecognition
```

### Issue: GUI doesn't display properly

**Solution**: Try updating CustomTkinter:
```bash
pip install --upgrade customtkinter
```

### Issue: Permission Denied (Linux/macOS)

**Solution**: Make the main script executable:
```bash
chmod +x main.py
python main.py
```

## Virtual Environment Management

### Activate Virtual Environment

**Windows**:
```bash
venv\Scripts\activate
```

**macOS/Linux**:
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Delete Virtual Environment

```bash
# Windows
rmdir /s venv

# macOS/Linux
rm -rf venv
```

## Upgrading Packages

To update all packages to latest versions:

```bash
pip install --upgrade -r requirements.txt
```

To update specific package:

```bash
pip install --upgrade customtkinter
```

## System-Specific Notes

### Windows
- Visual C++ Build Tools may be required for some packages
- Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

### macOS
- Ensure Xcode Command Line Tools are installed:
```bash
xcode-select --install
```

### Linux
- May require Python dev headers:
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev

# Fedora
sudo dnf install python3-devel
```

## Docker Installation (Optional)

To run in Docker:

1. Create a Dockerfile in project root:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

2. Build image:
```bash
docker build -t ai-math-assistant .
```

3. Run container:
```bash
docker run -it ai-math-assistant
```

## Verification Checklist

After installation, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] All packages installed successfully
- [ ] Application starts without errors
- [ ] GUI window displays correctly
- [ ] Chat interface is responsive
- [ ] All buttons are clickable
- [ ] Can process math operations

## Reinstalling from Scratch

If you encounter persistent issues:

1. **Remove virtual environment**:
```bash
deactivate
rm -rf venv
```

2. **Clear pip cache**:
```bash
pip cache purge
```

3. **Create fresh environment**:
```bash
python -m venv venv
```

4. **Activate and reinstall**:
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

5. **Run application**:
```bash
python main.py
```

## Getting Help

### Check Application Logs

The application creates `app.log` file with detailed error information:

```bash
# View last 50 lines of log
tail -n 50 app.log  # macOS/Linux
type app.log  # Windows (last 50 lines)
```

### Common Error Messages

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `TclError` | Reinstall customtkinter: `pip install --upgrade customtkinter` |
| `ImportError: No module named 'sklearn'` | Run `pip install scikit-learn` |
| `matplotlib: No module named tkinter` | Install tkinter (see Troubleshooting) |

## System Requirements

### Minimum
- CPU: Dual-core 1.5 GHz
- RAM: 2 GB
- Storage: 500 MB

### Recommended
- CPU: Quad-core 2.0 GHz
- RAM: 4 GB
- Storage: 1 GB

## Post-Installation Setup

### Optional: Add to PATH (Advanced Users)

Windows:
1. Right-click "This PC" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Add project folder to PATH

### Optional: Create Desktop Shortcut

**Windows**:
1. Create batch file `run.bat`:
```batch
@echo off
cd /d "%~dp0"
python main.py
```
2. Create shortcut to `run.bat`

**macOS/Linux**:
1. Create shell script `run.sh`:
```bash
#!/bin/bash
cd "$(dirname "$0")"
python main.py
```
2. Make executable: `chmod +x run.sh`

## Next Steps

After successful installation:

1. **Read README.md** for feature overview
2. **Launch the application** with `python main.py`
3. **Try basic operations** like "add 5 and 6"
4. **Explore all features** using the GUI buttons
5. **Check Statistics** to track your usage
6. **Export conversations** for records

## Support

For issues or questions:
1. Check this installation guide thoroughly
2. Review application logs in `app.log`
3. Verify all packages: `pip list`
4. Try reinstalling: `pip install -r requirements.txt --force-reinstall`

---

**Version**: 1.0  
**Last Updated**: 2026  
**Status**: Production Ready
