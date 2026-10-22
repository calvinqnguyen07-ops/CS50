def main():
    bill = float(input("Bill total: $"))
    percent = float(input("Tip percent: "))
    tip = bill * percent / 100
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${bill + tip:.2f}")


if __name__ == "__main__":
    main()
