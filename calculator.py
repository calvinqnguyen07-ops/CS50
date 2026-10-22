def calculate(x, op, y):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        return x / y
    raise ValueError("Unknown operator")


def main():
    while True:
        expression = input("Expression (e.g. 3 + 4) or q to quit: ").strip()
        if expression == "q":
            break
        try:
            x, op, y = expression.split()
            print(calculate(float(x), op, float(y)))
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
