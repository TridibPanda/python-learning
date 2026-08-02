student = {
    "Name": "Tridib",
    "Age": 25,
    "City": "Kolkata",
    "Company": "ABC",
    "Skills": ["React Native", "Flutter", "Python"],
}


print("Student Profile \n")
for key, value in student.items():
    if isinstance(value, list):
        print(f"{key}:\n\n{'\n\n'.join(value)}")
    else:
        print(f"{key}: {value}\n")
