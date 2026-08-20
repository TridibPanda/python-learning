class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


a = Number(10)
b = Number(20)
print(a + b)
# Output: 30 a + b -> a.__add__(b)-> self  = a , other = b -> self.value + other.value -> 10 + 20 -> 30
print(30 + 50)  # Output: 80 (30).__add__(50)
