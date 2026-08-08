# Create a class named Student and create an object of that class and assign it to a variable named student1. Then print the value of student1.
class Student:
    pass


# student1 is a reference variable that refers to an object of the Student class. The actual object is created in memory when Student() is executed.
student1 = Student()
print(student1)
# Output: <__main__.Student object at 0x102811a90>


student2 = Student()
print(student2)
# Output: <__main__.Student object at 0x109ba7250>

student3 = student1
"""
 student1 ───────────────┐
                         │
                         ▼
                   Object A (0x1001)

student3 ───────────────┘


student2 ───────────────► Object B (0x2001)
"""

student3.name = "Tridib"

print(student1.name)
# The output will be Tridib because student1 and student3 both refer to the same object in memory. When we execute student3.name = "Tridib", Python does not store the value in the variable student3; it stores the attribute name inside the shared object. Since student1 also points to the same object, accessing student1.name returns "Tridib" as well.
