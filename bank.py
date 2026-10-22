class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self._balance:.2f}"


def main():
    account = Account("Ana", 100)
    account.deposit(50)
    account.withdraw(30)
    print(account)

    try:
        account.withdraw(500)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
