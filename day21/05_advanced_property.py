class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # internal/protected attribute

    @property
    def age(self):
        print("GETTER called")
        return self._age

    @age.setter
    def age(self, value):
        print("SETTER called")

        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")

        self._age = value

    @age.deleter
    def age(self):
        print("DELETER called")
        del self._age


user = User("John", 25)

print("Initial age:")
print(user.age)  # Output: 25

print("\nUpdating age:")
user.age = 30
print(user.age)  # Output: 30

print("\nInvalid age:")
try:
    user.age = -10
except ValueError as error:
    print(error)  # Output: Age must be between 0 and 120

print("\nInvalid type:")
try:
    user.age = "30"
except TypeError as error:
    print(error)  # Output: Age must be an integer

print("\nDeleting age:")
del user.age

print("\nTrying to access deleted age:")
try:
    print(user.age)
except AttributeError as error:
    print(error)  # Output: 'User' object has no attribute '_age'
