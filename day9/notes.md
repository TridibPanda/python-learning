# OOP Question & Answer

### Q1. What happens when we create an object?
When an object is created, Python allocates memory for the object, initializes it, and returns a reference to that object. The variable stores the reference, not the actual object itself.

Memory Diagram
Memory Diagram
```text
Class

Student
   │
   │ Student()
   ▼

Object
----------------
Memory: 0x1001
----------------

    ▲
    │
student1
(reference variable)
```

### Q2. 
class Student:
    pass


student1 = Student()

student2 = student1

student2 = Student()

student2.name = "Rahul"

print(hasattr(student1, "name"))

Output: False
The output is False because student2 is reassigned to a newly created object. Initially, both student1 and student2 referred to the same object. However, after executing student2 = Student(), student2 starts referring to a new object, while student1 continues to refer to the original object. Therefore, the name attribute is added only to the new object, not to the original one.

### Q3.
class Student:
    pass


student1 = Student()

student2 = student1

student1 = None

student2 = None

Ans: After student2 = None, no reference points to the object anymore. The object becomes eligible for garbage collection. Python can then reclaim its memory because the object is no longer reachable.

### Q4. What is self?
self is a reference to the current object. Python automatically passes the current object's reference as the first argument to every instance method. Using self, we can access and modify the current object's attributes and methods.

### Q5. What is a Constructor?
A constructor is a special method that is automatically called when an object is created. It is mainly used to initialize the object's data. In Python, the constructor is implemented using the __init__() method.

### Q6. Why do we need self?
self represents the current object. It allows each object to access and store its own data and methods. Without self, Python would not know which object's attributes or methods are being accessed.

### Q7. Can we write another name instead of self?
Yes, we can use any name instead of self, but PEP 8 conventionally uses self. Using self is a widely accepted practice in the Python community, and it improves code readability and maintainability.

### Q8. Who passes self?
Python automatically passes the current object as the first argument when an instance method is called.

### Q9. Can we call __init__() directly?
Yes, we can call the __init__() method directly, but it is not recommended. The __init__() method is meant to be called automatically when an object is created. Calling it directly can lead to unexpected behavior and may not properly initialize the object.

### Q10. Can we create a constructor without self?
No, we cannot create a constructor without self. The self parameter is essential for instance methods, including the constructor, to access and modify the current object's attributes and methods. Without self, the constructor would not know which object's attributes to initialize, leading to errors and incorrect behavior.

### Q11. Can we create a constructor without parameters?
Yes, we can create a constructor without parameters. In such cases, the __init__() method will not take any arguments other than self. This is useful when we want to create objects with default values or when the object's attributes can be set later after the object is created. For example:
```python
class Student:
    def __init__(self):
        self.name = "Default Name"
        self.age = 18
```
### Q12. Can we create a constructor with parameters?
Yes, we can create a constructor with parameters. This allows us to initialize the object's attributes with specific values when the object is created. For example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
### Q13. Can we create multiple constructors in Python?
No, Python does not support method overloading, which means we cannot create multiple constructors with the same name but different parameters. However, we can achieve similar functionality by using default parameter values or by using variable-length arguments. For example:
```python
class Student:
    def __init__(self, name="Default Name", age=18):
        self.name = name
        self.age = age
```
### Q14. Can we create a constructor without __init__()?
No, in Python, the constructor is defined using the __init__() method. If we do not define an __init__() method, Python will provide a default constructor that does nothing.   

### Q15. Can we create a constructor with a different name?
No, in Python, the constructor must be named __init__(). This is a special method that is automatically called when an object is created. Using a different name for the constructor would not work, as Python would not recognize it as a constructor and would not call it when creating an object.