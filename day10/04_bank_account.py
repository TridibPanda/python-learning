# BankAccount class definition
class BankAccount:
    def __init__(self, account_holder, balance):  # Constructor method
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):  # Instance method
        print(f"Account Holder: {self.account_holder}")
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):  # Instance method
        self.balance += amount
        print(f"Amount deposited: {amount}")
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):  # Instance method
        self.balance -= amount
        print(f"Amount withdrawn: {amount}")
        print("Please collect your cash.")


account = BankAccount("Tridib", 10000)
account.show_balance()
account.deposit(5000)
account.withdraw(2000)
account.show_balance()
# Output: Account Holder: Tridib
# Output: Current balance: 10000
# Output: Amount deposited: 5000
# Output: New balance: 15000
# Output: Amount withdrawn: 2000
# Output: Please collect your cash.
# Output: Account Holder: Tridib
# Output: Current balance: 13000
