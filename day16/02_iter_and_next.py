numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30

print(numbers)  # Output: [10, 20, 30]

print(next(iterator))  # Output: raise exception StopIteration
