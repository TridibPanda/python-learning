student = {"name": "Tridib", "age": 25, "city": "Kolkata"}
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Kolkata'}
print(student["name"])
# Output: Tridib

# Add item in dictionary
student["company"] = "PwC"
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Kolkata', 'company': 'PwC'}

# Update item in dictionary
student["city"] = "Bangalore"
print(student)
# Output: {'name': 'Tridib', 'age': 25, 'city': 'Bangalore', 'company': 'PwC'}

for key, value in student.items():
    print(key, value)
# Output:
# name Tridib
# age 25
# city Bangalore
# company PwC
