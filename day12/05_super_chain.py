class Animal:
    def eat(self):
        print("Animal")


class Dog(Animal):
    def eat(self):
        print("Dog")
        super().eat()


class Breed(Dog):
    def eat(self):
        print("Breed")
        super().eat()


breed = Breed()

breed.eat()
# Output:
# Breed
# Dog
# Animal
