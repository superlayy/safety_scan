import os

# ===================== CONFIG =====================
ROOT_DIR = "."          # scan current directory
DELETE_FILES = True    # ⚠️ set to True to actually delete
# ==================================================

KEYWORDS = [
    "wallet",
    "private key",
    "seed",
    "mnemonic",
    "solana",
    "sol",
    "btc",
    "bitcoin",
    "bnb",
    "bsc",
    "ethereum",
    "eth",
    "metamask",
    "phantom",
    "trustwallet",
]

TEXT_EXTENSIONS = {
    ".txt", ".md", ".json", ".yaml", ".yml",
    ".env", ".csv", ".log", ".ini"
}

def contains_keyword(text: str) -> bool:
    text = text.lower()
    return any(k in text for k in KEYWORDS)

def scan():
    matched = []

    for root, _, files in os.walk(ROOT_DIR):
        for name in files:
            path = os.path.join(root, name)

            # check filename
            if contains_keyword(name):
                matched.append(path)
                continue

            # check content (text files only)
            ext = os.path.splitext(name)[1].lower()
            if ext in TEXT_EXTENSIONS:
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        if contains_keyword(f.read()):
                            matched.append(path)
                except Exception:
                    pass

    if not matched:
        print("✅ Done.")
        return

    print("\n⚠️  Matched files:")
    for f in matched:
        print(f)

    if DELETE_FILES:
        print("\n🔥 Deleting files...")
        for f in matched:
            try:
                os.remove(f)
                print(f"Deleted: {f}")
            except Exception as e:
                print(f"Failed: {f} ({e})")
    else:
        print("\n🧪 Dry run only — nothing deleted.")
        print("")

if __name__ == "__main__":
    scan()
