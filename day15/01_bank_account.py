# This class demonstrates basic encapsulation by bundling account data and the methods that operate on that data. We haven't yet added controlled access using properties/private attributes.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount:,}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.balance:,}")


account = BankAccount("Tridib", 10000)

account.show_balance()  # Output: Balance: 10,000

account.deposit(5000)
account.show_balance()  # Output: 15,000

account.withdraw(3000)  # Output: Withdrawn: 3,000
account.show_balance()  # Output: Balance: 12,000

account.withdraw(20000)  # Output: Insufficient balance
