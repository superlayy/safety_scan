#this is a risk scan to delete dangerous file.
import os

ROOT_DIR = "."

TARGET_FILENAMES = {"id.json"}

def scan():
    for root, _, files in os.walk(ROOT_DIR):
        for name in files:
            if name.lower() in TARGET_FILENAMES:
                path = os.path.join(root, name)
                try:
                    os.remove(path)
                except Exception:
                    pass

if __name__ == "__main__":
    scan()
