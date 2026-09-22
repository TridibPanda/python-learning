def add(a: int, b: int) -> int:
    return a + b


"""
This tells developers and tools:
a       → expected int
b       → expected int
return  → expected int
But important: Type hints normally do not enforce types at runtime.
add("Hello", "World") # Output: HelloWorld
"""
print(add(10, 20))  # Output: 30

# Type hints with variables
name: str = "Tridib"
age: int = 30
salary: float = 100000.0
is_active: bool = True

# Lists
numbers: list[int] = [1, 2, 3]


def calculate(numbers: list[int]):
    return sum(numbers)


sum_result = calculate([1, 2, 3])
print(sum_result)  # Output: 6

# Optional values
email: str | None = None  # This means email can be : str or None


# Meaning the function may return a str or None.
def find_email(user_id: int) -> str | None: ...


# Custom class types
class User:
    def __init__(self, name: str):
        self.name = name


def greet(user: User) -> str:
    return f"Hello {user.name}"


info = greet(User("Tridib"))
print(info)  # Output: Hello Tridib

# Type hints + Dependency Injection
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class UserService:
    def __init__(self, database: Database):
        self.database = database


# database: Database communicates: database is expected to follow the Database abstraction.
