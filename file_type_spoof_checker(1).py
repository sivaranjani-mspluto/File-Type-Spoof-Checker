
import os
import mimetypes

try:
    import magic  # magic is a third-party library
    USE_MAGIC = True
except ImportError:
    print("python-magic not found. Using mimetypes only (less accurate).")
    USE_MAGIC = False

def check_file_type(file_path):
    if not os.path.isfile(file_path):
        print(f"❌ FILE DOES NOT EXIST: {file_path}")
        return

    # Get extension-based MIME type
    ext_type, _ = mimetypes.guess_type(file_path)

    # Get actual MIME type from content
    if USE_MAGIC:
        actual_type = magic.from_file(file_path, mime=True)
    else:
        print("Install 'python-magic' for better accuracy!")
        actual_type = ext_type  # fallback

    print(f"📄 FILE: {file_path}")
    print(f"EXTENSION TYPE: {ext_type}")
    print(f"ACTUAL TYPE   : {actual_type}")

    if ext_type != actual_type:
        print("⚠️  WARNING: File extension does not match its content!")
    else:
        print("✅ File type matches its extension.")

# Example usage:
# Replace with your file path or use argparse for CLI
file_path = input("Enter the file path to check: ")
check_file_type(file_path)
