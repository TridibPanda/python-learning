# OOP Question & Answer

### Q1. What is Polymorphism?
Polymorphism is the ability to use the same interface or method name with different objects, where each object can provide its own behavior.

### Q2. What is Method Overriding?
Method overriding occurs when a child class provides its own implementation of a method already defined in its parent class. It enables polymorphism because the same method call can produce different behavior depending on the object.

### Q3. How is method overriding related to polymorphism?
Method overriding is a mechanism where a child class provides its own implementation of a parent method. It enables polymorphism because the same method call can produce different behavior depending on the object.

### Q4. What is duck typing in Python?
Duck typing is a Python approach where an object's suitability is determined by the methods and attributes it provides, rather than its specific class or inheritance relationship.

### Q5. Is duck typing a form of polymorphism? Explain the relationship.
Yes. Duck typing is a way of achieving polymorphic behavior in Python. Different types of objects can be passed to the same function as long as they provide the required interface or behavior.

### Q6. len() is the same function in all three cases. Why can it work with a str, list, and tuple?
len() is a polymorphic built-in function that works with different objects as long as those objects provide a way to determine their length.

### Q7. What is operator overloading in Python?
Operator overloading is the ability to define how operators such as +, -, ==, or < behave for objects of a user-defined class by implementing special methods such as __ add__, __ eq__, and __ lt__.

### Q8. Why is __ add__() called a special/dunder method?
__ add__() is a special/dunder method that Python invokes when the + operator is used with an object.
__ add__() is implemented by types that support the + operation. Built-in types such as int, str, and list provide their own implementations, and we can define __ add__() in our own classes to customize + for our objects.

### Q9. Why do we need __ eq__() here? What happens if we don't define it?
If a class does not define __ eq__(), equality comparison still works using the inherited/default behavior. Defining __ eq__() allows us to customize what equality means for our objects.

### Q10. What is the purpose of __ eq__()?
__eq__() is a special method used to customize the behavior of the == operator for objects of a class.

### Q11. Comparison Operator Overloading.
Python provides special methods such as __ eq__(), __ lt__(), and __ gt__() to customize comparison operators for user-defined objects.
```Text
== → __eq__()
< → __lt__()
> → __gt__()
```
is checks object identity, while == checks equality using the class's __ eq__() implementation or inherited/default behavior.

### Q12. What is __ str__() in Python?
__ str__() is a special method that defines the human-readable string representation of an object. It is commonly used by print() to display meaningful information about a custom object.

### Q13. What is __ repr__()?
__repr__() defines a developer-oriented, unambiguous representation of an object, mainly useful for debugging and inspection.

Difference: __ str__() is intended to be user-friendly, while __ repr__() is intended to be informative for developers. If __ str__() isn't defined, Python can fall back to __ repr__() for string conversion.

### Q14. What must __ len__() return? How does __ len__() demonstrate polymorphism in Python?
__ len__() must return a non-negative integer representing the length/size of the object.

len() demonstrates polymorphism because the same built-in function can work with different types of objects, and each type can provide its own length behavior through __ len__().

### Q15. What is __ getitem__() used for in Python?
__ getitem__() is a special method that allows objects to support indexing and item access using the [] syntax.

### Q16. What is __ contains__() used for?
__ contains__() is a special method that allows a custom object to support membership testing using the in operator.

***
```Text
+       → __add__()
==      → __eq__()
<       → __lt__()
>       → __gt__()
print   → __str__()
repr()  → __repr__()
len()   → __len__()
obj[0]  → __getitem__()
x in obj → __contains__()
```
***