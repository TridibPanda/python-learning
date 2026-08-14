class Parent:
    def __init__(self):
        self.__value = "Parent"  # Private variable
        self._name = "Tridib"  # Protected variable


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "Child"  # Private variable
        self._name = "Babu"  # using protected variable from Parent class

    def show(self):
        print(self._name)  # Child's name
        print(self.__value)  # Child's value
        print(self._Parent__value)  # Parent's value

        self._Parent__value = "Changed"  # Changing Parent's private variable

        print(self._Parent__value)


obj = Child()

obj.show()
# Output:
# Babu
# Child
# Parent

print(obj._name)  # Accessing protected variable from outside the class
# print(obj.__value) Error: 'Child' object has no attribute '__value' Why: Private variables are name mangled in Python
print(obj._Parent__value)  # Accessing Parent's private variable from outside the class
