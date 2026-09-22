# What is a decorator?
# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function.
# Decorators are often used to modify the behavior of functions or methods without changing their code.
# They are a powerful tool in Python and are widely used in web frameworks, logging, authentication, and more.


def greet():
    print("Hello")


def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


greet = my_decorator(greet)
greet()
# Output:
# Before function
# Hello
# After function
"""
The important flow is:
greet
  ↓
my_decorator(greet)
  ↓
wrapper function returned
  ↓
greet now refers to wrapper
  ↓
greet()
  ↓
Before
  ↓
original greet()
  ↓
After
"""


# @ syntax
# Instead of: greet = my_decorator(greet)
# we normally write :
@my_decorator
def greet_func():
    print("Hello World")


greet_func()
# Output:
# Before function
# Hello World
# After function


# Decorator with arguments
# The previous decorator only works with a function having no arguments.
# Our decorator needs to support arguments:
def my_decorator_arg(func):
    def wrapper(*args, **Kwargs):
        print("Before Function")
        result = func(*args, **Kwargs)
        print("After function")
        return result

    return wrapper


# Why *args, **kwargs?
# Because we don't know what arguments the original function may accept.
# *args allows the decorator to accept any number of positional arguments.
# **kwargs allows the decorator to accept any number of keyword arguments.


@my_decorator_arg
def greet_arg(name):
    print(f"Hello {name}")


greet_arg("Tridib")
# Output:
# Before function
# Hello Tridib
# After function


# Returning the original result
@my_decorator_arg
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
# Output:
# Before function
# After function
# 30
"""
print()
→ "Show this NOW"

return
→ "Give this value BACK to whoever called me"

That's the entire reason for the different output order.
"""

# functools.wraps
# There's one more important decorator concept. When we wrap a function, Python can lose some metadata about the original function.
# So we commonly use:
from functools import wraps


def my_decorator_wraps(func):

    @wraps(func)
    def wrapper(*args, **Kwargs):
        print("Before")
        result = func(*args, **Kwargs)
        print("After")
        return result

    return wrapper


# what is @wraps(func)?
# @wraps(func) is a decorator from the functools module that is used to preserve the metadata of the original function when it is wrapped by another function (the decorator).
# When you create a decorator, the wrapper function replaces the original function, and without @wraps(func), the metadata of the original function (such as its name, docstring, and other attributes) would be lost.
# @wraps(func) preserves important metadata such as the original function's: name , docstring, metadata
# This becomes particularly useful when building real applications and frameworks.


@my_decorator_wraps
def calculate(numbers: list[int]):
    return sum(numbers)


result = calculate([20, 30, 50])
print(result)
# Output
# Before
# After
# 100

"""
Where decorators are useful
Common examples:
Logging
Authentication / authorization
Timing
Caching
Validation
Retry logic
Permissions
"""


# Parameterized decorator
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello")


say_hello()
# Output:
# Hello
# Hello
# Hello

# Decorator can modify behavior
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result

    return wrapper


@timer
def calculate_timer():
    total = 0

    for i in range(1_000_000):
        total += i
    return total


result = calculate_timer()
print(result)
# Output:
# Execution time: 0.04108691215515137
# 499999500000


# Authentication-style decorator
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access denied")
            return
        return func(user, *args, **kwargs)

    return wrapper


@require_admin
def delete_user(user):
    print("User deleted")


delete_user("admin")  # Output: User deleted
delete_user("Tridib")  # Output: Access denied


# # Multiple decorators
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One - Before")
        result = func(*args, **kwargs)
        print("Decorator One - After")
        return result

    return wrapper


def decorator_two(func):

    def wrapper(*args, **kwargs):
        print("Decorator Two - Before")
        result = func(*args, **kwargs)
        print("Decorator Two - After")
        return result

    return wrapper


@decorator_one
@decorator_two
def greet_multi():
    print("Hello")


greet_multi()
# Output:
# Decorator One - Before
# Decorator Two - Before
# Hello
# Decorator Two - After
# Decorator One - After


# Decorators on methods
def log_call(func):

    def wrapper(*args, **kwargs):
        print("Method called")
        return func(*args, **kwargs)

    return wrapper


class User:
    @log_call
    def login(self):
        print("User logged in")


user = User()
user.login()
# Output:
# Method called
# User logged in

# Other built-in/common decorators : @property, @classmethod, @staticmethod, @abstractmethod, @wraps

"""
          DECORATOR
              │
       ┌──────▼──────┐
       │   Before    │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │ Original     │
       │ Function     │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │    After    │
       └─────────────┘
This pattern appears everywhere in backend frameworks—for example authentication, logging, timing, authorization, caching, retries, and route registration.
"""
