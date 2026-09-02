def numbers():
    yield from range(5)


gen = numbers()

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

for value in gen:
    print(value)

# Output:
# 2
# 3
# 4


def squares(n):
    for i in range(n):
        yield i * i


print(list(squares(5)))
# Output: [0, 1, 4, 9, 16]
