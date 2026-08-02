# This function demonstrates the use of try-except blocks in Python. It prompts the user to input a number and attempts to convert it to an integer. If the user inputs a non-integer value, it raises a ValueError, which is caught by the except block, and an appropriate error message is printed.
def try_except_fn():
    try:
        number = int(input("Enter a number: "))
        print(number)
    except ValueError:
        print("Please enter a valid number.")


try_except_fn()
# Output: Input: abc
# Output: Please enter a valid number.
# Input: 5
# Output: 5
