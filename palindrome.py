def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def main():
    text = input("Text: ")
    if is_palindrome(text):
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
