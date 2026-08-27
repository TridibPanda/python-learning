class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def show_balance(self):
        print(f"{self.owner}: {self.balance}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Savings withdrawal")
        super().withdraw(amount)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Current withdrawal")
        super().withdraw(amount)


accounts = [SavingsAccount("Tridib", 10000), CurrentAccount("Rahul", 20000)]

for account in accounts:
    account.withdraw(1000)
    account.show_balance()

# Output:
# Savings withdrawal
# Tridib: 9000
# Current withdrawal
# Rahul: 19000
# Why is this an example of polymorphism?
# Polymorphism allows the same interface or method call to work with objects of different classes, with each object providing its own implementation.
