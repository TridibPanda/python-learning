class Animal:  # Parent class / Base class / Superclass
    def __init__(self, name):  # Constructor
        self.name = name

    def eat(self):  # Instance method
        print(f"{self.name} is eating")


class Dog(Animal):  # Child class / Derived class / Subclass
    def bark(self):  # Instance method
        print(f"{self.name} is barking")


dog = Dog("Bruno")

# Accessing the inherited attribute from the parent class
print(dog.name)  # Output: Bruno
# Calling methods from the parent class through the child class instance
dog.eat()  # Output: Bruno is eating
# Calling method from the child class
dog.bark()  # Output: Bruno is barking
