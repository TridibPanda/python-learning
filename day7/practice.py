# 1. Invalid Input check using try except block
def invalid_input_fn():
    try:
        number = int(input("Enter a number: "))
        print(number)
    except ValueError:
        print("Invalid Input")


invalid_input_fn()
# Output: Input: abc
# Output: Invalid Input
# Output: Input: 5
# Output: 5


# 2. Calculator using try except block
def calculator():
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} x {b} = {a * b}")
        print(f"{a} / {b} = {a / b}")
    except ValueError:
        print("Invalid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


calculator()
# Output: Input: 10, 0
# Output:  10 + 0 = 10
# Output:  10 - 0 = 10
# Output:  10 x 0 = 0
# Output:  Cannot divide by zero.


# 3. Custom Exception for Insufficient Balance
class EnoughBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise EnoughBalanceError("Not enough balance.")
    elif amount < 100:
        raise ValueError("Withdrawal amount must equal or greater than 100.")
    balance -= amount
    print(f"Amount withdrawn: {amount}")
    print("Please collect your cash.")
    print(f"Remaining balance: {balance}")
    return balance


# 4. Function to handle amount withdrawal with exception handling
def amount_withdrawal():
    balance = 10000
    try:
        amount = int(input("Enter amount to withdraw: "))
        withdraw(balance, amount)
    except EnoughBalanceError as e:
        print(e)
    except ValueError as e:
        print(e)


amount_withdrawal()
# Output: Input: 1500
# Output: Not enough balance.
# Output: Input: 500
# Output: Amount withdrawn: 500
# Output: Please collect your cash.
# Output: Remaining balance: 500
