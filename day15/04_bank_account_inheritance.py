class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

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

    def show_balance(self):
        print(f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.deposit(interest)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount


savings = SavingsAccount("Tridib", 10000)
current = CurrentAccount("Rahul", 20000)

savings.add_interest(5)

print(savings.balance)  # Output: 10500.0
print(current.balance)  # Output: 20000

current.deposit(10000)
current.show_balance()  # Output: Balance: 30000

current.withdraw(5000)
current.show_balance()  # Output: Balance: 25000
