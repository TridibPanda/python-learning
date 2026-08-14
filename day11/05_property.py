# Property Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):  # Getter for balance
        return self.__balance

    @balance.setter
    def balance(self, value):  # Setter for balance
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")


account = BankAccount(1000)
print(account.balance)  # Output: 1000

account.balance = 5000
print(account.balance)  # Output: 5000

account.balance = -500  # Output: Balance cannot be negative
print(account.balance)  # Output: 5000
