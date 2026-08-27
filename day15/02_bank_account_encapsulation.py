class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount:,}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.__balance:,}")


account = BankAccount("Tridib", 10000)

print(account.balance)  # Output: 10000

account.deposit(5000)
print(account.balance)  # Output: 15000

account.withdraw(3000)  # Output: Withdrawn: 3,000
print(account.balance)  # Output: 12000
