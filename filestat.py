import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Count lines, words and characters in a file")
    parser.add_argument("filename", help="path to a text file")
    parser.add_argument("-l", "--lines", action="store_true", help="count lines")
    parser.add_argument("-w", "--words", action="store_true", help="count words")
    parser.add_argument("-c", "--chars", action="store_true", help="count characters")
    args = parser.parse_args()

    try:
        with open(args.filename) as file:
            text = file.read()
    except FileNotFoundError:
        sys.exit("File not found")

    show_all = not (args.lines or args.words or args.chars)

    if args.lines or show_all:
        print("Lines:", len(text.splitlines()))
    if args.words or show_all:
        print("Words:", len(text.split()))
    if args.chars or show_all:
        print("Characters:", len(text))


if __name__ == "__main__":
    main()
