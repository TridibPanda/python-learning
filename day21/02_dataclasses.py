# What is dataclasses in Python?
# Dataclasses is a module introduced in Python 3.7 that provides a decorator and functions for automatically adding special methods to user-defined classes. It simplifies the process of creating classes that are primarily used to store data by automatically generating methods like __init__, __repr__, __eq__, and others based on the class attributes.
"""
dataclass
→ primarily represents/stores data

normal class
→ more customized behavior/design
"""

from dataclasses import dataclass


# The @dataclass decorator is used to define a dataclass. It automatically generates the __init__ method based on the class attributes, allowing you to create instances of the class with the specified attributes.
@dataclass
class User:
    name: str
    age: int
    email: str


user1 = User("John", 25, "john@example.com")
user2 = User(name="Alice", age=30, email="alice@example.com")

print(user1)  # Output: User(name='John', age=25, email='john@example.com')
print(user2)  # Output: User(name='Alice', age=30, email='alice@example.com')

print(user1.name)  # Output: John
print(user1.age)  # Output: 25
print(user1.email)  # Output: john@example.com

print(user1 == user2)  # Output: False
