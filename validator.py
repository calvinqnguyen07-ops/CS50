import re

PATTERNS = {
    "email": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "phone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "zip": r"\d{5}(-\d{4})?",
}


def validate(kind, value):
    return re.fullmatch(PATTERNS[kind], value) is not None


def main():
    kind = input("Check (email/phone/zip): ").strip().lower()
    if kind not in PATTERNS:
        print("Unknown type")
        return

    value = input("Value: ").strip()
    if validate(kind, value):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
