from _decimal import Decimal


class Account:
    def __init__(self, name: str, balaance: Decimal):
        self.name = name
        self.set_balance(balaance)

    @property
    def balance(self):
        return self.balance

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance is not valid")
        self.balance= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            raise ValueError("You want to scam us")
        self.balance -= amount