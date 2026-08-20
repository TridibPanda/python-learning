class Student:
    def __init__(self, subjects):
        self.subjects = subjects

    def __contains__(self, item):
        return item in self.subjects


student = Student(["Python", "JavaScript", "React"])

print("Python" in student)
# Output: True "Python" in student--> student.__contains__("Python")--> self = student, item = "Python" --> True
print("Java" in student)
# Output: False "Java" in student--> student.__contains__("Java") --> self = student, item = "Java" --> False
