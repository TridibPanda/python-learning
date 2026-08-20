class Student:
    def __init__(self, subjects):
        self.subjects = subjects

    def __getitem__(self, index):
        return self.subjects[index]


student = Student(["Python", "JavaScript", "React"])

print(student[0])
# Output: Python student[0]--> student.__getitem__(0)--> self = student , index = 0 ---> Python
print(student[1])
# Output: JavaScript student[1]--> student.__getitem__(1)--> self = student , index = 1 ---> JavaScript
