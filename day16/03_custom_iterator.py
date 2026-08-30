# CountUp is an iterator because it implements both __iter__() and __next__(). __next__() produces one value at a time and maintains the iteration state using self.current. When there are no more values, it raises StopIteration.
class CountUp:
    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    # __iter__() makes the object usable as an iterator/iterable in iteration contexts such as for
    def __iter__(self):
        return self

    # __next__() defines how the next value is produced.
    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


counter = CountUp(3)

print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
