import os

TEXT = "Your lucky numbers are 4, 8, 15. You will never see them \u2014 your context was truncated."

def main():
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "gate: 1-140 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
