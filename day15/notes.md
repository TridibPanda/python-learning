```text
BankAccount
│
├── Class variable
│   └── bank_name
│
├── Class method
│   └── change_bank_name()
│
├── Constructor
│   └── __init__()
│
├── Instance variables
│   ├── owner
│   └── __balance
│
├── Encapsulation
│   └── __balance
│
├── Property
│   └── balance
│
├── Property setter
│   └── validation
│
├── Abstract method
│   └── withdraw()
│
├── Concrete method
│   ├── deposit()
│   └── show_balance()
│
└── Inheritance
    │
    ├── SavingsAccount
    │     └── withdraw()
    │
    └── CurrentAccount
          └── withdraw()
```

#### Encapsulation:
Encapsulation bundles data and the methods that operate on that data inside a class, while controlling how that data is accessed or modified.

#### Abstraction 
Abstraction exposes the required interface/behavior (what needs to be done) while hiding implementation details (how it is done). In an abstract class, the child class provides the implementation of the required abstract methods.

#### What is the difference between encapsulation and abstraction in Python?
Encapsulation controls access to data by bundling it with the methods that operate on it, whereas abstraction hides implementation details and exposes only the required interface.

#### What is the difference between method overriding and method overloading in Python?
Method overriding: A child class provides its own implementation of a method already defined in its parent class.

Method overloading: Using the same method name with different parameter lists. Python does not support traditional method overloading; it can be simulated using default arguments or *args.

Operator overloading: Defining how operators behave for user-defined objects using special methods such as __add__(), __eq__(), __lt__(), etc.

```text
Overriding
Parent → speak()
Child  → speak()
         ↑
      same method
      different implementation


Overloading
add(a, b)
add(a, b, c)
↑
same method name
different parameters


Operator Overloading
a + b
 ↓
__add__()
```

#### What is the difference between @classmethod and @staticmethod in Python?
A class method receives cls and is generally used to work with class-level data or class-level behavior. A static method receives neither self nor cls automatically and is used when the operation does not depend on a particular instance or class.

#### Why does Python use @staticmethod if we can simply define a normal function inside a class without self? What does the decorator actually change?
@staticmethod tells Python that the function should not receive the instance (self) automatically when accessed through an object. Without it, a normal function defined in a class becomes an instance method when accessed through an instance.

#### Can a staticmethod be called using both the class and an instance? If yes, explain what happens in each case.
A static method can be called through both the class and an instance. In both cases, Python does not automatically pass self or cls; it simply executes the underlying function with the arguments explicitly provided.

#### What is name mangling in Python? Why does self.__value become _ClassName__value?
Name mangling is Python's mechanism for transforming an attribute with a double leading underscore (__) into a name containing the class name, such as _Student__value. It helps prevent accidental access and name collisions, particularly in inheritance, but it is not true privacy.

#### What is the difference between __str__() and __repr__() in Python?
__str__() defines the human-readable string representation of an object, while __repr__() defines a developer-oriented representation useful for debugging. print() prefers __str__(), and if __str__() is not defined, Python falls back to __repr__().

#### What is the difference between == and is in Python?
is checks object identity—whether two references point to the same object. == checks value/equality, typically through the __eq__() method, whose behavior can be customized for user-defined classes.

#### What is duck typing in Python? Explain why it is considered a form of polymorphism.
Duck typing is a Python approach where an object's suitability is determined by the methods and attributes it provides rather than its specific class or inheritance relationship. It is a form of polymorphism because the same operation can be performed on different object types, with each object providing its own behavior.