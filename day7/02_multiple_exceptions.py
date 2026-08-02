# This function demonstrates handling multiple exceptions in Python. It prompts the user to input two numbers and attempts to divide them. If the user inputs a non-integer value, it raises a ValueError, and if the user tries to divide by zero, it raises a ZeroDivisionError. The function catches these exceptions and prints appropriate error messages.
def multiple_exception():
    try:
        a = int(input("A: "))
        b = int(input("B: "))

        print(a / b)
    except ValueError:
        print("Invalid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


multiple_exception()
# Output: Input: 10, 0
# Output: Cannot divide by zero.
# Input: 10, abc
# Output: Invalid number.
# Input: 10, 2
# Output: 5.0
