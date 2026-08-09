# Instance Method in Python
class Student:
    def __init__(self, name):  # Constructor method
        self.name = name

    def introduce(self):  # Instance method
        print(f"My name is {self.name}")


student1 = Student("Tridib")
student2 = Student("Rahul")

# Calling instance methods
student1.introduce()
student2.introduce()
# Output: My name is Tridib
# Output: My name is Rahul

# Modifying the instance variable
student1.name = "Amit"
student1.introduce()
# Output: My name is Amit
