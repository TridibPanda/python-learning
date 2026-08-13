class Student:
    school = "ABC School"

    def __init__(self, name):  # Constructor method
        self.name = name

    @classmethod
    def show_school(cls):  # Class method
        print(cls.school)

    @classmethod
    def change_school(cls, new_school):  # Class method to change the class variable
        cls.school = new_school


student1 = Student("Tridib")

student1.show_school()  # Output: ABC School (accessing the class variable through an instance)
Student.show_school()  # Output: ABC School (accessing the class variable directly through the class)

Student.change_school(
    "XYZ School"
)  # Changing the class variable using the class method
student1.show_school()  # Output: XYZ School (the class variable has been changed)
Student.show_school()  # Output: XYZ School (the class variable has been changed)
