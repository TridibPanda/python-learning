class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):  # Human-readable
        return f"Student: {self.name}, Marks: {self.marks}"

    def __repr__(self):  # Developer/debugging representation
        return f"Student(name={self.name!r}, marks={self.marks!r})"


student = Student("Tridib", 90)

print(student)  # Output: Student: Tridib, Marks: 90
# print(student) --> string representation requested --> student.__str__() --> self = student --> self.name   → "Tridib" self.marks  → 90 --> "Student: Tridib, Marks: 90"
print(repr(student))  # Output: Student(name='Tridib', marks=90)
# print(repr(student)) --> student.__repr__() --> self = student --> self.name   → "Tridib" self.marks  → 90 --> Student(name='Tridib', marks=90)
