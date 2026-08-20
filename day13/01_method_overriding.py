# Method Overriding and Polymorphism
# Method overriding allows child classes to provide their own implementation of a parent method.
# This enables polymorphism: calling the same method on different objects produces different behaviors.

# Base class with a speak() method
class Animal:
    def speak(self):
        print("Animal sound")


# Dog overrides speak() with its own implementation
class Dog(Animal):
    def speak(self):
        print("Woof")


# Cat overrides speak() with its own implementation
class Cat(Animal):
    def speak(self):
        print("Meow")


# Create objects of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Same method name, different behaviors - this is POLYMORPHISM
animal.speak()  # Output: Animal sound
dog.speak()  # Output: Woof
cat.speak()  # Output: Meow

# Example of polymorphic behavior:
# We can treat all these objects as Animal and call speak() on each
animals = [animal, dog, cat]
for obj in animals:
    obj.speak()  # Each object responds with its own speak() implementation
# Output:
# Animal sound
# Woof
# Meow
