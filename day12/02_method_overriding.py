class Animal:  # Parent class / Base class / Superclass
    def eat(self):  # Instance method
        print("Animal is eating")


class Dog(Animal):  # Child class / Derived class / Subclass
    def eat(self):  # Overriding the eat method from the parent class
        print("Dog is eating")


animal = Animal()
dog = Dog()

animal.eat()  # Output: Animal is eating
dog.eat()  # Output: Dog is eating (the method from the Dog class overrides the method from the Animal class)
