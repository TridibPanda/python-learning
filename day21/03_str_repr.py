class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r}, email={self.email!r})"


user = User("Tridib", 25, "tridib@example.com")

print("str:")
print(str(user))
# Output:
# str:
# Tridib (25)

print("\nrepr:")
print(repr(user))
# Output:
# repr:
# User(name='Tridib', age=25, email='tridib@example.com')

print("\nprint object:")
print(user)
# Output:
# print object:
# Tridib (25)

print("\nlist:")
print([user])
# Output:
# list:
# [User(name='Tridib', age=25, email='tridib@example.com')]

# If you're designing a production class, what kind of information should __str__() contain, and what kind of information should __repr__() contain?
# __str__() should be concise and human-readable, containing the information useful when displaying the object to a user.
# __repr__() should be detailed and unambiguous, containing enough information to understand or debug the object's state.
"""
__str__
  ↓
Human / readable
  ↓
print(obj), str(obj)


__repr__
  ↓
Developer / debugging
  ↓
repr(obj), containers like [obj]


print([obj])
  ↓
list asks each element for repr()
  ↓
obj.__repr__()
"""
