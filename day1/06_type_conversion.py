# User Input Age with Type Conversion
age = int(input("Enter your age: "))

print(type(age))
# Output: <class 'int'>

# User Input Salary with Type Conversion
salary = float(input("Enter salary: "))

print(type(salary))
# Output: <class 'float'>

print(f"You are {age} years old and your salary is {salary:,}.")
# Output: You are <user_input> years old and your salary is <user_input>.
