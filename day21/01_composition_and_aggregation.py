# what is composition and aggregation in python
# Composition is a strong form of association where one object contains another object as a part of its structure. If the container object is destroyed, the contained object is also destroyed.
# Composition represents strong ownership: the contained object's lifecycle is conceptually tied to the owner.
# Aggregation is a weaker form of association where one object contains another object, but the contained object can exist independently of the container.
"""
Composition
→ object creates/owns the contained object
→ strong ownership relationship

Aggregation
→ object receives/uses existing objects
→ contained object can exist independently
"""

print("--- Composition ---")


class Engine:
    def start(self):
        print("Engine started")


# Composition : The Car class has an Engine object as a part of its composition. The Engine is created and managed by the Car class, and it cannot exist independently of the Car. When the Car is created, it automatically creates an Engine instance.
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()
# Output:
# Engine started
# Car started

print("\n--- Aggregation ---")


# Aggregation: The Department class has a list of Employee objects, but the Employee objects can exist independently of the Department. The Department class does not manage the lifecycle of the Employee objects; they can be created and destroyed independently.
class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def show_employees(self):
        for employee in self.employees:
            print(employee.name)


employee1 = Employee("John")
employee2 = Employee("Alice")

employees = [employee1, employee2]

department = Department("Engineering", employees)

department.show_employees()
# Output:
# John
# Alice
