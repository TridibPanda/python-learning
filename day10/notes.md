# OOP Question & Answer

### Q1. What is an instance method?
An instance method is a function defined inside a class that operates on an instance of that class. It has access to the instance's attributes and can modify them. The first parameter of an instance method is usually named `self`, which refers to the instance of the class on which the method is called.

### Q2. Why does an instance method need self?
The `self` parameter in an instance method is a reference to the current instance of the class. It allows the method to access and modify the attributes and methods of that specific instance. Without `self`, the method would not know which instance's data it should operate on, making it impossible to work with instance-specific information.

### Q3. What is an instance variable?
An instance variable is a variable that is defined within a class and is specific to each instance of that class. Each object created from the class has its own copy of the instance variables, allowing them to hold different values for different instances. Instance variables are typically initialized in the constructor method (`__init__`) and are accessed using the `self` keyword.

### Q4. What happens when we call:
```python
class Student:
    def __init__(self, name):  # Constructor method
        self.name = name

    def introduce(self):  # Instance method
        print(f"My name is {self.name}")


student1 = Student("Tridib")
student1.introduce()
```
When we call `student1.introduce()`, the following happens:
1. Python looks for the `introduce` method in the `Student` class.
2. The method is called with `student1` as the first argument, which is passed to the `self` parameter of the method.
3. Inside the `introduce` method, we can access the attributes of `student1` using `self`, allowing us to perform actions or return values specific to that instance. The method executes its code and may return a value or perform an action based on the instance's state.

### Q5. What is the difference between: student1 is student2 and student1 == student2?
- `student1 is student2`: This checks if both `student1` and `student2` refer to the exact same object in memory. It returns `True` if they are the same object, and `False` otherwise.
- `student1 == student2`: This checks if the values of `student1` and `student2` are equal, based on the implementation of the `__eq__` method in the class. By default, it checks for object identity (i.e., whether they are the same object), but it can be overridden to compare the contents of the objects instead.

### Q6. Why do different objects have different values for the same instance variable?
Each object has its own instance attributes, so different objects can maintain different values for the same attribute.