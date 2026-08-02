# Simple calculator
first_number = int(input("Enter first number for calculation: "))
second_number = int(input("Enter second number for calculation: "))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return "Can't divide by zero" if b == 0 else a / b


print(f"Addition: {add(first_number, second_number)}")
print(f"Subtraction: {subtract(first_number, second_number)}")
print(f"Multiplication: {multiply(first_number, second_number)}")
print(f"Division: {divide(first_number, second_number)}")
# Output: input: 10, 5
# Output: Addition: 15
# Output: Subtraction: 5
# Output: Multiplication: 50
# Output: Division: 2.0


# Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = int(input("Enter a number for factorial calculation: "))
print(f"Factorial: {factorial(number)}")
# Output: input: 5
# Output: Factorial: 120
