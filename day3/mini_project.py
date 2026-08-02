# This is a simple for loop that prints a triangle pattern of asterisks.
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# This is another way to print a triangle pattern of asterisks using nested loops.
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

secret_number = 7
# This is a simple guessing game that uses a while loop to allow the user to guess a secret number.
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations!")
        break
    else:
        print("Try Again")
# Output: If the user guesses the secret number, the output will be:
# Congratulations!
