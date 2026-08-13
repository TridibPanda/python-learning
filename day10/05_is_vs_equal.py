class Student:
    pass


student1 = Student()
student2 = Student()
student3 = student1

# Comparing the Student objects using the 'is' operator and the '==' operator
print(student1 is student2)
print(student1 == student2)
# Output: False
# Output: False

print(student1 is student3)
print(student1 == student3)
# Output: True
# Output: True


class Employee:
    def __init__(self, name):
        self.name = name


employee1 = Employee("Tridib")
employee2 = Employee("Tridib")

# Comparing the Employee objects using the 'is' operator and the '==' operator
print(employee1 is employee2)
print(employee1 == employee2)
# Output: False
# Output: False
