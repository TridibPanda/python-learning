# This is a simple example of using return statements in Python functions.


def add(a, b):
    return a + b


result = add(10, 20)
print(result)
# Output: 30


def subtract(a, b):
    return a - b


result = subtract(20, 10)
print(result)
# Output: 10


def multiply(a, b):
    return a * b


result = multiply(10, 20)
print(result)
# Output: 200


def divide(a, b):
    return "Can't divide by zero" if b == 0 else a / b


result = divide(20, 0)
print(result)
# Output: Can't divide by zero

result = divide(20, 10)
print(result)
# Output: 2.0
