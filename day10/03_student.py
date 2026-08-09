# Student class definition
class Student:
    def __init__(self, name, age, course):  # Constructor method
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):  # Instance method
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

    def study(self):  # Instance method
        print(f"I am studying {self.course}")


student1 = Student("Tridib", 25, "Python")
student2 = Student("Rahul", 26, "React Native")

# Calling instance methods
student1.introduce()
student1.study()
student2.introduce()
student2.study()
# Output: My name is Tridib
# Output: I am 25 years old
# Output: I am studying Python
# Output: My name is Rahul
# Output: I am 26 years old
# Output: I am studying React Native
