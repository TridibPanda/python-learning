# This is a simple example of variable scope in Python.
company = "PwC"


# This is a simple example of global variable scope in Python.
def show_company():
    print(company)


show_company()
# Output: PwC
print(company)
# Output: PwC


# This is a simple example of local variable scope in Python.
def test():
    age = 25
    print(age)


# print(age) Output: NameError: name 'age' is not defined
test()
# Output: 25
