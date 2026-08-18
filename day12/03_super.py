class Animal:  # Parent class / Base class / Superclass
    def eat(self):  # Instance method
        print("Animal is eating")


class Dog(Animal):  # Child class / Derived class / Subclass
    def eat(self):  # Overriding the eat method from the parent class
        print("Dog is eating")
        super().eat()  # Calling the eat method from the parent class using super()


dog = Dog()
dog.eat()
# Output:
# Dog is eating
# Animal is eating (the method from the parent class is called using super())
