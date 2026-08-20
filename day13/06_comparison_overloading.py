class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks


student1 = Student(80)
student2 = Student(80)
student3 = Student(90)

print(student1 == student2)
# Output: True  student1 == student2 --> student1.__eq__(student2)--> self = student1 , other = student2--> self.marks == other.marks--> 80 == 80 --> True

print(student1 < student3)
# Output: True  student1 < student3 --> student1.__lt__(student3)--> self = student1 , other = student3--> self.marks < other.marks--> 80 < 90 --> True

print(student3 < student2)
# Output: False  student3 < student2 --> student3.__lt__(student2)--> self = student3 , other = student2--> self.marks < other.marks--> 90 < 80 --> False

print(student1 > student3)
# Output: False  student1 > student3 --> student1.__gt__(student3)--> self = student1 , other = student3--> self.marks > other.marks--> 80 > 90 --> False

print(student3 > student2)
# Output: True  student3 > student2 --> student3.__gt__(student2)--> self = student3 , other = student2--> self.marks > other.marks--> 90 > 80 --> True
