class Student:
    pass


student1 = Student()
student2 = Student()
student3 = student1

# Checking identity using 'id()' function
print(id(student1))
print(id(student2))
print(id(student3))
# Output: 4379440016
# Output: 4379777680
# Output: 4379440016

# Checking identity using 'is' operator
print(student1 is student2)
print(student1 is student3)
# Output: False
# Output: True
