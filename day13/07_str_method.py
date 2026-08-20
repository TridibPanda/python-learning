class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"


student = Student("Tridib", 90)
print(student)  # Output: <__main__.Student object at 0x102241a90> [ without __str__()]
print(student)  # Output: Student: Tridib, Marks: 90 [with __str__()]
# print(student) --> string representation requested --> student.__str__() --> self = student --> self.name   → "Tridib" self.marks  → 90 --> "Student: Tridib, Marks: 90"
