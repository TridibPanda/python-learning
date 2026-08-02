# 1. This is a simple example of defining and calling functions in Python.
def say_hello(name):
    print(f"Hello {name}")


say_hello("Tridib")
# Output: Hello Tridib


# 2. Square of a number
def find_square(number):
    return number**2


number = int(input("Enter a number for square calculation: "))
result = find_square(number)
print(result)
# Output: input: 4
# Output: 16


# 3. Cube of a number
def find_cube(number):
    return number**3


number = int(input("Enter a number for cube calculation: "))
result = find_cube(number)
print(result)
# Output: input: 3
# Output: 27


# 4. Check if a number is even or odd
def is_even(number):
    return number % 2 == 0


number = int(input("Enter a number for even/odd check: "))
result = is_even(number)
print(result)
# Output: input: 4
# Output: True


# 5. Student information with default company
def student_info(name, age, company="ABC"):
    print("Student Information\n")
    print(f"Name: {name}\n\nAge: {age}\n\nCompany: {company}")


student_info("Tridib", 25)
# Output: Student Information
# Name: Tridib
# Age: 25
# Company: ABC
