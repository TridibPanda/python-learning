class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Savings account withdrawal")
        super().withdraw(amount)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Current account withdrawal")
        super().withdraw(amount)


savings = SavingsAccount("Tridib", 10000)
current = CurrentAccount("Rahul", 20000)

savings.withdraw(2000)
# Output: Savings account withdrawal
# Withdrawn: 2000
current.withdraw(5000)
# Output: Current account withdrawal
# Withdrawn: 5000

print(savings.balance)  # Output: 8000
print(current.balance)  # Output: 15000
