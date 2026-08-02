# This function demonstrates the use of the raise statement in Python. It prompts the user to input their age and checks if it is below 18. If the age is below 18, it raises a ValueError with a custom message. The function catches this exception and prints an appropriate error message.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Eligible")


def raise_example():
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except ValueError as e:
        print(f"Error: {e}")


raise_example()
# Output: Input: 16
# Output: Error: Age must be 18 or above.
# Input: 20
# Output: Eligible
