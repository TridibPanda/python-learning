# User Input Student Profile
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
favorite_programming_language = input("Enter your favorite programming language: ")

# Output Student Profile
print("-" * 30)
print("Student Profile")
print("-" * 30)
print(f"Name     : {full_name}")
print(f"Age      : {age}")
print(f"City     : {city}")
print(f"Language : {favorite_programming_language}")
print(f"\n Next year you will be {age + 1} years old.")
