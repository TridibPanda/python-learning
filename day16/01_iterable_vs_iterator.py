numbers = [10, 20, 30]

print(numbers)  # Output: [10, 20, 30]

iterator = iter(numbers)

print(iterator)  # Output: <list_iterator object at 0x10556f340>

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
print(next(iterator))  # Output: raise exception StopIteration
