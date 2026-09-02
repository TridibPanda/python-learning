def count_up(max_value):
    current = 1

    while current <= max_value:
        yield current
        current += 1


numbers = count_up(3)

print(numbers)  # Output: <generator object count_up at 0x105d9dd80>

print(next(numbers))  # Output: 1
print(next(numbers))  # Output: 2
print(next(numbers))  # Output: 3
