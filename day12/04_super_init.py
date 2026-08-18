class Animal:
    # Constructor of the Animal class that takes name as a parameter
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    # Constructor of the Dog class that takes name and breed as parameters
    def __init__(self, name, breed):
        # Calling the constructor of the parent class to initialize the name attribute
        super().__init__(name)
        self.breed = breed


dog = Dog("Bruno", "Labrador")

print(dog.name)  # Output: Bruno (the name attribute is inherited from the Animal class)
print(dog.breed)  # Output: Labrador (the breed attribute is specific to the Dog class)
