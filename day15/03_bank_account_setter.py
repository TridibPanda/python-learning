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

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount


account = BankAccount("Tridib", 10000)

print(account.balance)  # Output: 10000

account.balance = 15000
print(account.balance)  # Output: 15000

account.deposit(5000)
print(account.balance)  # Output: 20000

account.withdraw(3000)
print(account.balance)  # Output: 17000

account.balance = -100  # Output: ValueError: Balance cannot be negative
