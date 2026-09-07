# Without using 'with' statement (This requires you to explicitly close the file after writing to it )
file = open("demo.txt", "w")

try:
    file.write("Hello Python")
finally:
    file.close()


# Using 'with' statement (This automatically closes the file after the block of code is executed )
with open("demo.txt", "w") as file:
    file.write("Hello Python with 'with' statement")
