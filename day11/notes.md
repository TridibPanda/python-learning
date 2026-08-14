# OOP Question & Answer

### Q1. What is a class variable?
A class variable is a variable that is shared among all instances of a class. It is defined within the class but outside of any instance methods. Class variables are used to store data that is common to all instances of the class, and they can be accessed using the class name or through any instance of the class. Changes made to a class variable will affect all instances of the class.

**Example:**
```python
class Student:
    school = "ABC School"  # Class variable - shared by all instances

    def __init__(self, name):
        self.name = name  # Instance variable - unique to each instance


# Access class variable
print(Student.school)  # Output: ABC School

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)  # Output: ABC School
print(s2.school)  # Output: ABC School

# All instances share the same class variable
Student.school = "XYZ School"
print(s1.school)  # Output: XYZ School
print(s2.school)  # Output: XYZ School
```

### Q2. When would you use a class variable instead of an instance variable?
I use a class variable when a piece of data should be shared across all instances of a class, such as a common configuration, constant-like value, or a class-wide counter. I use an instance variable when the data belongs specifically to an individual object and can differ between instances.

**Example:**
```python
class Car:
    total_cars = 0  # Class variable - shared counter

    def __init__(self, brand, color):
        self.brand = brand  # Instance variable - unique to each car
        self.color = color  # Instance variable - unique to each car
        Car.total_cars += 1  # Increment shared counter


c1 = Car("Toyota", "Red")
c2 = Car("Honda", "Blue")
c3 = Car("BMW", "Black")

print(Car.total_cars)  # Output: 3
print(c1.brand)  # Output: Toyota
print(c2.brand)  # Output: Honda
```

### Q3. What is a class method in Python?
A class method is a method that is bound to the class and not the instance of the class. It takes the class itself as its first argument, which is conventionally named `cls`. Class methods are defined using the `@classmethod` decorator. They can access and modify class variables and are often used for factory methods or to provide alternative constructors.

**Example:**
```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def total_persons(cls):
        return f"Total persons: {cls.count}"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name)  # Alternative constructor


p1 = Person("Alice")
p2 = Person("Bob")
print(Person.total_persons())  # Output: Total persons: 2

p3 = Person.from_birth_year("Charlie", 1990)
print(Person.total_persons())  # Output: Total persons: 3
```

### Q4. What's the difference between self and cls in Python?
In Python, `self` refers to the instance of the class and is used to access instance variables and methods. It is the first parameter of instance methods. On the other hand, `cls` refers to the class itself and is used in class methods to access class variables and methods. It is the first parameter of class methods. While `self` is used for instance-level operations, `cls` is used for class-level operations.

**Example:**
```python
class Example:
    class_var = "I'm a class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def instance_method(self):
        return f"Instance: {self.instance_var}"  # self accesses instance data

    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"  # cls accesses class data


obj = Example("I'm an instance variable")
print(obj.instance_method())  # Output: Instance: I'm an instance variable
print(Example.class_method())  # Output: Class: I'm a class variable
```

### Q5. Why do we use @classmethod?
We use the `@classmethod` decorator to define a method that is bound to the class rather than an instance of the class. This allows us to access and modify class variables, create alternative constructors, and perform operations that are relevant to the class as a whole. Class methods can be called on the class itself or on instances of the class, making them versatile for various use cases.

**Example:**
```python
class Database:
    connection_string = "localhost:5432"

    def __init__(self, user):
        self.user = user

    @classmethod
    def set_connection(cls, host, port):
        cls.connection_string = f"{host}:{port}"

    @classmethod
    def get_connection(cls):
        return cls.connection_string


print(Database.get_connection())  # Output: localhost:5432
Database.set_connection("192.168.1.1", "3306")
print(Database.get_connection())  # Output: 192.168.1.1:3306

db = Database("admin")
print(db.get_connection())  # Output: 192.168.1.1:3306
```

### Q6. What is the difference between an instance method and a class method?
An instance method receives the current object as self and is generally used to work with instance-specific data. A class method receives the class as cls and is used when the operation works with class-level data or behavior. A class method is defined using the @classmethod decorator.

**Example:**
```python
class Employee:
    company = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):  # Instance method
        return f"{self.name} works at {self.company} with salary {self.salary}"

    @classmethod
    def change_company(cls, new_company):  # Class method
        cls.company = new_company


e1 = Employee("Alice", 50000)
print(e1.display_info())  # Output: Alice works at Tech Corp with salary 50000

Employee.change_company("Innovation Inc")
print(e1.display_info())  # Output: Alice works at Innovation Inc with salary 50000
```

### Q7. Can a class method access instance variables? 
No, a class method cannot access instance variables directly because it does not have access to the instance (self). Class methods can only access class variables and other class methods. If you need to work with instance variables, you should use an instance method instead.

**Example:**
```python
class MyClass:
    class_var = "Class Variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @classmethod
    def access_class_var(cls):
        return cls.class_var  # This works

    @classmethod
    def try_access_instance_var(cls):
        # return cls.instance_var  # This would fail - NameError
        return "Class method cannot access instance variables"


obj = MyClass("Instance Variable")
print(MyClass.access_class_var())  # Output: Class Variable
print(
    MyClass.try_access_instance_var()
)  # Output: Class method cannot access instance variables
``` 
.
### Q8. Can a class method access instance variables indirectly?
Yes, a class method can access instance variables indirectly by creating an instance of the class within the class method. However, this is not a common practice and is generally discouraged, as it can lead to confusion and unexpected behavior. It is better to use instance methods for operations that require access to instance variables.

**Example:**
```python
class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def show_name(cls, student):
        print(student.name)


student1 = Student("Tridib")

Student.show_name(student1)
# Output: Tridib
```      


### Q9. Can an instance method access class variables?
Yes, an instance method can access class variables. Since instance methods have access to the class through the instance (self), they can reference class variables using either the class name or the instance itself.

**Example:**
```python
class Student:
    school = "XYZ School"  # Class variable

    def __init__(self, name):
        self.name = name

    def display_info(self):
        # Access class variable through self
        return f"{self.name} studies at {self.school}"

    def display_info_alt(self):
        # Access class variable through class name
        return f"{self.name} studies at {Student.school}"


s1 = Student("Alice")
print(s1.display_info())  # Output: Alice studies at XYZ School
print(s1.display_info_alt())  # Output: Alice studies at XYZ School
```
### Q10. What is static method in Python? Why use @staticmethod?
A static method is a method that belongs to a class but does not have access to the instance (self) or the class (cls). It is defined using the @staticmethod decorator. Static methods are used for utility functions that perform a task in isolation, without needing to access or modify class or instance data. They can be called on the class itself or on instances of the class.

@staticmethod is used when a method is logically related to a class but doesn't need access to either instance-specific data or class-level data. The decorator prevents Python from automatically passing self or cls.

### Q10. can an static method access class variables and instance variables?
No, a static method cannot access class variables or instance variables directly because it does not receive the instance (self) or the class (cls) as parameters. Static methods are designed to perform tasks that are independent of the class or instance state. If you need to access class or instance variables, you should use class methods or instance methods instead.

### Q11. can static method access class data and instance data indirectly?
Yes, a static method can access class data and instance data indirectly by creating an instance of the class within the static method or by passing an instance as an argument to the static method. However, this is not a common practice and is generally discouraged, as it can lead to confusion and unexpected behavior. It is better to use class methods or instance methods for operations that require access to class or instance data.
**Example:**
```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_name(student):
        print(student.name)

    @staticmethod
    def show_school():
        print(Student.school)


Student.show_school()
# Output: ABC School
student1 = Student("Tridib")
Student.show_name(student1)
# Output: Tridib
```

#### INSTANCE METHOD
```text
def method(self):
       ↓
self → Object
        ↓
Can work with instance data
Can also access class data
```

#### CLASS METHOD
```text
@classmethod
def method(cls):
        ↓
cls → Class
        ↓
Works with class-level data
No automatic instance reference
```

#### STATIC METHOD
```text
@staticmethod
def method(a, b):
        ↓
No automatic self
No automatic cls
        ↓
Independent operation logically grouped inside class
```

### Q12. What is Encapsulation in OOP?
Encapsulation is an OOP principle of bundling data and the methods that operate on that data within a class, while controlling how that data is accessed or modified. In Python, this can be implemented using conventions such as _, name mangling with __, and properties with getters and setters.

### Q13. What is the difference between _value and __value in Python?
A single leading underscore is a convention indicating that an attribute is intended for internal or protected-style use, but Python doesn't enforce it. A double leading underscore triggers name mangling, changing a name like __value to _ClassName__value. Name mangling helps prevent accidental name collisions, particularly when inheritance is involved.

### Q14. What is the difference between public, private, and protected access modifiers in Python?
In Python, access modifiers are not enforced by the language but are indicated by naming conventions:
- **Public**: Attributes and methods are accessible from anywhere. They have no leading underscores (e.g., `value`).
- **Protected**: Attributes and methods are intended for internal use within the class and its subclasses. They are indicated by a single leading underscore (e.g., `_value`).
- **Private**: Attributes or methods with a double leading underscore trigger name mangling. This makes direct access using the original name unavailable and helps prevent accidental access or name collisions, especially with inheritance.

### Q15. Can a subclass access a parent's __private attribute?
No, a subclass cannot directly access a parent's private attribute (indicated by a double leading underscore) due to name mangling. However, it can access it indirectly through public or protected methods provided by the parent class. The private attribute is still part of the parent class, but its name is changed to include the class name, making it inaccessible using its original name in the subclass.

### Q16. What does @property do?
@property allows a method to be accessed like an attribute and is commonly used to provide controlled read access to internal data.

### Q17. What does @property.setter do?
A setter provides controlled write access to an internal attribute and can perform validation or other logic before updating it.

### Q18. Why would you use @property instead of directly exposing a public variable?
It provides controlled access to attributes while allowing validation, computation, or other logic during reading or writing, without changing the external attribute-style interface.