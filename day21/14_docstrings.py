# What is  docstrings?
# Docstrings are a way to document your code in Python.
# They are string literals that appear right after the definition of a function, method, class, or module.
# Docstrings provide a convenient way to associate documentation with Python code, making it easier for developers to understand the purpose and usage of the code.

# A docstring is a string used to document a module, class, function, or method.

# Module docstring
"""Utilities for working with users."""


# Function docstring
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)
# output: Return the sum of two numbers.
# help(add)


# Class docstring
class Users:
    """Represent a user of the application."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Users.__doc__)
# Output: Represent a user of the application.

# Module docstring
print(__doc__)
# Output: Utilities for working with users.


# Why are docstrings useful?
# Suppose you have this:
def calculate_total_doc(price, tax): ...


# After six months, another developer sees this function.
# They might wonder:
# What does price represent?
# Is tax a percentage or actual amount?
# What does the function return?
# Can it raise an exception?
# A good docstring can explain this.


# Example:
def calculate_total(price: float, tax: float) -> float:
    """
    Calculate the final price including tax.

    Args:
        price: Original price before tax.
        tax: Tax amount as a decimal percentage.

    Returns:
        Final price including tax.

    Raises:
        ValueError: If price or tax is negative.
    """

    if price < 0 or tax < 0:
        raise ValueError("Price and tax cannot be negative")

    return price + (price * tax)


# Now someone can use:
print(calculate_total.__doc__)
# OR
# help(calculate_total)
# and understand how to use the function without reading its implementation.


# Docstrings in Agentic AI / FastAPI
def search_documents(query: str) -> list:
    """
    Search documents relevant to the user's query.

    Args:
        query: User's search query.

    Returns:
        A list of relevant documents.
    """
    return []


# Docstrings help developers understand tools/functions and their intended behavior.
# In frameworks and tooling ecosystems, documentation metadata can also be consumed by introspection or tooling. But don't assume that simply writing a docstring automatically makes an AI model understand your implementation. The exact behavior depends on the framework/tooling.


class Calculator:
    """Perform basic mathematical operations."""

    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b


print(Calculator.__doc__)
# Output: Perform basic mathematical operations.
print(Calculator.add.__doc__)
# Output: Return the sum of two numbers.

"""
User management utilities.
"""


class User:
    """Represent a user in the application."""

    def __init__(self, name: str, age: int):
        """Initialize a user with a name and age."""
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Return a short introduction for the user."""
        return f"My name is {self.name} and I am {self.age} years old."


def create_user(name: str, age: int) -> User:
    """
    Create and return a User object.

    Args:
        name: Name of the user.
        age: Age of the user.

    Returns:
        A new User object.
    """
    return User(name, age)


if __name__ == "__main__":
    user = create_user("Tridib", 28)

    print(user.introduce())

    print("\nClass docstring:")
    print(User.__doc__)

    print("\nMethod docstring:")
    print(User.introduce.__doc__)

    print("\nFunction docstring:")
    print(create_user.__doc__)
