# ATM Application
class EnoughBalanceError(Exception):
    pass


initial_balance = 10000


# Function to deposit amount with exception handling
def deposit(balance, amount):
    if amount < 100:
        raise ValueError("Deposit amount must equal or greater than 100.")
    balance += amount
    print(f"Amount deposited: {amount}")
    print(f"New balance: {balance}")
    return balance


# Function to withdraw amount with exception handling
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


# Function to check balance
def check_balance(balance):
    print(f"Current balance: {balance}")


# Function to perform ATM operations with exception handling
def atm_operations():
    balance = initial_balance
    while True:
        print("\nATM Operations:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance = deposit(balance, amount)
            except ValueError as e:
                print(f"Error: {e}")
            finally:
                print("Deposit operation completed. Thank you for using our ATM.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                balance = withdraw(balance, amount)
            except ValueError as e:
                print(f"Error: {e}")
            except EnoughBalanceError as e:
                print(f"Error: {e}")
            finally:
                print("Withdrawal operation completed. Thank you for using our ATM.")

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            print("Exiting ATM. Thank you!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


atm_operations()


# Additional Function to Safely Divide Two Numbers with Exception Handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division not possible.")
        return None


def divide_numbers():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = safe_divide(a, b)
        if result is not None:
            print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")


divide_numbers()
