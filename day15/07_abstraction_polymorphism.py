from abc import ABC, abstractmethod


# Encapsulation + Inheritance + Abstraction + Polymorphism
class BankAccount(ABC):
    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"{self.owner}: {self.balance}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        print("Savings withdrawal")


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        print("Current withdrawal")


accounts = [
    SavingsAccount("Tridib", 10000),
    CurrentAccount("Rahul", 20000),
]

for account in accounts:
    account.withdraw(1000)
    account.show_balance()

# Output:
# Savings withdrawal
# Tridib: 9000
# Current withdrawal
# Rahul: 19000
# Explain how abstraction and polymorphism work together in this example.
# Abstraction defines the required interface/contract; polymorphism allows different concrete implementations of that interface to be used through the same method call.

print(BankAccount.bank_name)  # Output: ABC Bank
BankAccount.change_bank_name("XYZ Bank")
print(BankAccount.bank_name)  # Output: XYZ Bank
# self refers to the current instance/object, while cls refers to the current class. Instance methods use self; class methods use cls.
