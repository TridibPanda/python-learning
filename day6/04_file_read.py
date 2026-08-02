# This code demonstrates how to read the contents of a file in Python using the `with` statement, which automatically handles closing the file after its block of code is executed.
with open("day6/sample.txt", "r") as file:
    content = file.read()
    print(content)

# The following code snippet shows an alternative way to read a file without using the `with` statement. In this case, you need to manually close the file after reading its contents to free up system resources.
file = open("day6/sample.txt", "r")
content = file.read()
print(content)
file.close()
