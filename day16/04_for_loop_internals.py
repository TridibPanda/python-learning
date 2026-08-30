numbers = [10, 20, 30]

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30

# The for loop is conceptually doing:
iterator = iter(numbers)

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30


# Custom iterator
class CountUp:
    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter = CountUp(3)

for number in counter:
    print(number)

# Output:
# 1
# 2
# 3
