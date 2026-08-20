# Different classes with the same interface (speak method) - this enables polymorphism

# Classes with the same method name but different implementations
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


class Robot:
    def speak(self):
        print("Beep")


# Function that works with ANY object that has a speak() method - POLYMORPHIC FUNCTION
def make_it_speak(obj):
    obj.speak()


# Create objects of different types
dog = Dog()
cat = Cat()
robot = Robot()

# Same function, different behavior based on object type - this is POLYMORPHISM
make_it_speak(dog)  # Output: Woof
make_it_speak(cat)  # Output: Meow
make_it_speak(robot)  # Output: Beep
