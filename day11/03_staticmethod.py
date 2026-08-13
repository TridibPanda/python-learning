class Student:
    school = "ABC School"

    def __init__(self, name):  # Constructor method
        self.name = name

    def introduce(self):  # Instance method
        return f"My name is {self.name}"

    @classmethod
    def change_school(cls, school):  # Class method to change the class variable
        cls.school = school

    @staticmethod
    def add(a, b):  # Static method to add two numbers
        return a + b


student = Student("Tridib")
print(
    student.introduce()
)  # Output: My name is Tridib (calling the instance method using an instance)

Student.change_school("XYZ School")
print(student.school)
# Output: XYZ School (accessing the class variable through an instance after changing it using a class method)

print(student.add(10, 20))  # Output: 30 (calling the static method using an instance)
print(
    Student.add(30, 20)
)  # Output: 50 (calling the static method using the class name)
