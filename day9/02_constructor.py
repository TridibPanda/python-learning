# A constructor is a special method that is automatically called when an object of a class is created
class Employee:
    def __init__(self):
        print("Constructor Called")


employee = Employee()

# Output: Constructor Called


# self represents the current object. It allows each object to access and store its own data and methods. Without self, Python would not know which object's attributes or methods are being accessed.
class Student:
    def __init__(self):
        print("self :", self)

        self.name = "Tridib"

        print(self.name)


student = Student()

print("student :", student)

print(student.name)
# Output:
# self : <__main__.Student object at 0x102811a90>
# Tridib
# student : <__main__.Student object at 0x102811a90>
# Tridib


# Update name attribute of staff object
class Staff:
    def __init__(self):
        self.name = "Tridib"

        print(self.name)


staff = Staff()

staff.name = "Rahul"

print(staff.name)
# Output:
# Tridib
# Rahul
