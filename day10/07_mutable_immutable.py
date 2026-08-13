# int / float / string / bool -> immutable (why? because we cannot change the value of these types after they have been created)
x = 5
y = x  # y now references the same integer object as x
x = 10  # This creates a new integer object and assigns it to x, but the original integer 5 remains unchanged
print(y)  # Output: 5

# List -> mutable (why? because we can change the values of the list after it has been created)
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# Tuple -> immutable (why? because we cannot change the values of the tuple after it has been created)
numbers_tuple = (1, 2, 3)
# numbers_tuple[0] = 4  # This will raise a TypeError because tuples are immutable
print(numbers_tuple)  # Output: (1, 2, 3)

# Set -> mutable (why? because we can add or remove elements from the set after it has been created)
numbers_set = {1, 2, 3}
numbers_set.add(4)
print(numbers_set)  # Output: {1, 2, 3, 4}

# Dictionary -> mutable (why? because we can change the values of the dictionary after it has been created)
student = {"name": "Tridib", "age": 25}
student["age"] = 26
student["city"] = "Mumbai"
print(student)  # Output: {"name": "Tridib", "age": 26, "city": "Mumbai"}

# Mutable vs Immutable
# Ans: A mutable object can be modified after creation without creating a new object, while an immutable object's value cannot be changed after creation. Any apparent change to an immutable value results in a new object/reference.
