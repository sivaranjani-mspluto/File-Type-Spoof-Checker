# 🛡️ File Type Spoof Checker

**File Type Spoof Checker** is a simple Python tool that detects whether a file's actual content matches its extension. This helps identify files that are **masquerading** as something else — a common technique used by malware to bypass filters or trick users.

---

## Features

- Detects mismatches between file extension and content
- Uses MIME type comparison for accurate detection
- Flags suspicious files (e.g., `.jpg` file that's really an `.exe`)
- Optionally uses `python-magic` for better content detection

---

## Why This Matters

Attackers often rename dangerous files (like `.exe`, `.js`) with safe-looking extensions (like `.jpg`, `.pdf`) to fool users or bypass security systems.

This tool helps detect such **spoofed files**, making it a useful addition to your **basic malware analysis** or **file forensics** workflow.

---

## Requirements

- Python 3.x

Install dependencies (recommended):
```bash
pip install python-magic-bin  # For Windows
```
```bash
#For Linux/macOS
pip install python-magic
sudo apt install libmagic1  # Required for linux systems
```
## ✅ Sample Output:
![image alt](https://github.com/sivaranjani-mspluto/File-Type-Spoof-Checker/blob/main/OutputScreenshot%202025-07-03%20074251.jpg)

![image alt](https://github.com/sivaranjani-mspluto/File-Type-Spoof-Checker/blob/main/output2Screenshot%202025-07-03%20075409.jpg)

