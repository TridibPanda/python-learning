class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    # The __eq__() method is used to compare two objects for equality. It should return True if the objects are considered equal, and False otherwise.
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    # hash() is used to get the hash value of an object, which is used in hash-based collections like sets and dictionaries.
    def __hash__(self):
        return hash(self.user_id)

    def __repr__(self):
        return f"User(id={self.user_id!r}, name={self.name!r})"


user1 = User(1, "John")
user2 = User(1, "John")
user3 = User(2, "Mike")

print("Equality:")
print(user1 == user2)  # Output: True
print(user1 == user3)  # Output: False

print("\nHash:")
print(hash(user1))  # Output: 1
print(hash(user2))  # Output: 1
print(hash(user3))  # Output: 2

print("\nSet:")
users = {user1, user2, user3}
print(users)  # Output: {User(id=1, name='John'), User(id=2, name='Mike')}

print("\nDictionary:")
user_map = {user1: "Admin", user3: "User"}

print(user_map[user2])  # Output: Admin

# A value used to calculate an object's hash should not change while that object is being used as a set element or dictionary key.
"""
__eq__ defines:
"When are two objects equal?"

__hash__ defines:
"Which hash bucket should this object belong to?"

             Object
                │
       ┌────────┴────────┐
       ↓                 ↓
    __eq__()          __hash__()
       │                 │
       ↓                 ↓
 "Are they equal?"   "Where to look?"
       │                 │
       └────────┬────────┘
                ↓
       dict / set lookup
"""
