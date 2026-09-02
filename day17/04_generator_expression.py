numbers = (x * 2 for x in range(5))

print(numbers)  # Output: <generator object <genexpr> at 0x100566b50>

print(type(numbers))  # Output: <class 'generator'>

print(next(numbers))  # Output: 0
print(next(numbers))  # Output: 2

for number in numbers:
    print(number)
# Output:
# 4
# 6
# 8
