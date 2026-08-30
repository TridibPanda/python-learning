class EvenNumbers:
    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


numbers = EvenNumbers(6)

for number in numbers:
    print(number)

# Output:
# 0
# 2
# 4
# 6
# __iter__() returns an iterator, while __next__() returns the next value and maintains the iterator's state. When no values remain, __next__() raises StopIteration.
