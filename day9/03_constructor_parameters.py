# parameters are used to pass values to the constructor when creating an object. These parameters allow us to initialize the object's attributes with specific values at the time of creation.
class Student:
    def __init__(self, name, age):

        print("self :", self)

        self.name = name  # Copy the value from the local variable name into the current object's attribute name.

        self.age = age


student = Student("Tridib", 25)

print(student.name)

print(student.age)
# Output:
# self : <__main__.Student object at 0x102811a90>
# Tridib
# 25
