def count_up(max_value):
    current = 1

    while current <= max_value:
        print(f"Before yield: current = {current}")

        yield current

        print(f"After yield: current = {current}")
        current += 1


numbers = count_up(3)

print("Generator created")

print(next(numbers))
print(next(numbers))
print(next(numbers))
# Output:
# Generator created
# Before yield: current = 1
# 1
# After yield: current = 1
# Before yield: current = 2
# 2
# After yield: current = 2
# Before yield: current = 3
# 3
