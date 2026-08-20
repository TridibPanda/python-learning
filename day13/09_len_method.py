class Student:
    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


student = Student(["Python", "JavaScript", "React"])

print(len(student))  # Output: 3
# len(student) --> student.__len__() --> self = student --> self.subjects --> ["Python", "JavaScript", "React"]  --> 3
