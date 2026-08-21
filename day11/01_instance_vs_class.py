class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name, age):  # Constructor method
        self.name = name  # Instance variable
        self.age = age  # Instance variable


# Creating two instances of the Student class
student1 = Student("Tridib", 25)
student2 = Student("Rahul", 26)

# Accessing instance variables
print(student1.name)  # Output: Tridib
print(student2.name)  # Output: Rahul

# Accessing class variable
print(student1.school)  # Output: ABC School
print(student2.school)  # Output: ABC School

# Modifying the class variable using instance
student1.school = "XYZ School"

# Accessing class variable after modification
print(student1.school)
# Output: XYZ School (instance variable takes precedence over class variable)
print(student2.school)
# Output: ABC School (instance variable not modified, so it uses the class variable)
print(Student.school)  # Output: ABC School (accessing the class variable directly)
