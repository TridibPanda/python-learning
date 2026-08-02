student = {"name": "Tridib", "age": 25, "city": "Kolkata"}
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Kolkata'}
print(student["name"])
# Output: Tridib

# Add item in dictionary
student["company"] = "ABC"
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Kolkata', 'company': 'ABC'}

# Update item in dictionary
student["city"] = "Bangalore"
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Bangalore', 'company': 'ABC'}

for key, value in student.items():
    print(key, value)
# Output:
# name Tridib
# age 25
# city Bangalore
# company ABC
