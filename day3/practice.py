# 1. This is a simple for loop that prints numbers from 1 to 20.
for i in range(1, 21):
    print(i)
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

# 2. This is a for loop that prints even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# Output: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

# 3. This is a for loop that prints odd numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
# Output: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19


# 4. This is a for loop that prints the multiplication table of the input number.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# Output: If the number is 5, the output will be:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
