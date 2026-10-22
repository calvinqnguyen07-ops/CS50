import sys
from collections import Counter


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python wordcount.py filename.txt")

    try:
        with open(sys.argv[1]) as file:
            words = file.read().lower().split()
    except FileNotFoundError:
        sys.exit("File not found")

    cleaned = [w.strip(".,!?;:\"'()") for w in words]
    counts = Counter(w for w in cleaned if w)

    for word, count in counts.most_common(10):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
