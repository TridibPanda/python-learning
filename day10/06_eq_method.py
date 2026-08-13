# Defining the __eq__ method to compare Student objects based on their names
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


student1 = Student("Tridib")
student2 = Student("Tridib")
student3 = Student("Rahul")

# Comparing the Student objects using the 'is' operator and the '==' operator
print(student1 is student2)  # Output: False
print(student1 == student2)  # Output: True
print(student1 is student3)  # Output: False
print(student1 == student3)  # Output: False
