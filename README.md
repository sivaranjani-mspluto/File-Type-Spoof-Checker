# 🛡️ File Type Spoof Checker

A simple Python tool that checks if a file’s **actual content type** matches its **file extension**. Helps detect spoofed or misleading files — a common tactic in malware delivery.

---

## 🔍 What It Does

- Compares file extension type (e.g., `.jpg`) with actual file content
- Flags suspicious files where types don’t match
- Uses `python-magic` for accurate MIME detection (optional)

---

## ⚙️ How to Use

```bash
python file_type_spoof_checker.py path/to/your/file
