import secrets
import string


def generate(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    length = int(input("Length: "))
    print(generate(length))


if __name__ == "__main__":
    main()
