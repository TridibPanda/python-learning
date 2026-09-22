class User:
    # What is __slots__?
    # Ans: It's a special attribute that allows you to explicitly declare the attributes that an object of the class can have.
    # It can help save memory by preventing the creation of a default __dict__ for each instance, which is used to store instance attributes.
    # Instead, it uses a more compact structure to store the declared attributes.
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("John", 30)

print(user.name)  # Output: John
print(user.age)  # Output: 30

print("\nAdding new attribute:")

try:
    user.email = "John@example.com"
except AttributeError as error:
    print(error)

# Output:
# 'User' object has no attribute 'email' and no __dict__ for setting new attributes


class NormalUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age


normal_user = NormalUser("Mike", 25)

normal_user.email = "mike@example.com"

print("\nNormal class:")
print(normal_user.email)  # Output: mike@example.com

# Imagine we have 100,000 User objects, and every object only ever needs: name, age
# Why could __slots__ be useful in this situation?
# Ans:  __slots__ can reduce per-instance memory overhead by avoiding the normal instance __dict__ and using a more compact storage mechanism for the declared attributes.

"""
The 3 things to remember about __slots__
__slots__
   │
   ├── 1. Restricts allowed instance attributes
   │
   ├── 2. Usually removes instance __dict__
   │
   └── 3. Can reduce memory usage per object

"""
