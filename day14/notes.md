# OOP Question & Answer

### Q1. What is abstraction?
Abstraction is an OOP principle of exposing the essential interface or behavior while hiding implementation details. It allows a base class to define what operations subclasses must provide, while the subclasses define how those operations are implemented.

### Q2. Q1. What is ABC and @abstractmethod ? What does @abstractmethod tell Python?
ABC is a helper base class from Python's abc module used to create abstract base classes.

@abstractmethod marks a method as abstract and requires concrete subclasses to provide an implementation before they can be instantiated.

@abstractmethod tells Python that any subclass must override and implement that method. If a subclass fails to provide an implementation, Python will block you from creating an instance of that subclass.

### Q3. What is Concrete method?
Concrete method: A method that has an actual implementation/body and is not abstract.

Instance method: A method that operates on an instance and receives self as its first parameter.
***
```Text
                METHOD
                  │
        ┌─────────┴─────────┐
        │                   │
   How it works        Does it have
   with object/class?  implementation?
        │                   │
   ┌────┼────┐          ┌───┴────┐
   │    │    │          │        │
instance class static concrete abstract
method  method method   method   method
```
***

### Abstract vs Concrete Method
```Text
Abstract method
    ↓
No concrete implementation provided
    ↓
Subclass must implement it


Concrete method
    ↓
Has an actual implementation
    ↓
Subclass can directly inherit it
```

```Text
┌─────────────────────────────────────┐
│          OOP — 4 PILLARS            │
├─────────────────────────────────────┤
│                                     │
│  1. Encapsulation    ✅             │
│     Data + controlled access        │
│                                     │
│  2. Inheritance      ✅             │
│     Child reuses parent             │
│                                     │
│  3. Polymorphism     ✅              │
│     Same interface, different       │
│     behavior                        │
│                                     │
│  4. Abstraction      ✅             │
│     Define WHAT, hide HOW           │
│                                     │
└─────────────────────────────────────┘
For example:

Payment (ABC)
    │
    ├── encapsulates payment data
    │
    ├── inherited by UPI/Card classes
    │
    ├── abstract pay() defines the contract
    │
    └── different pay() implementations
             ↓
        polymorphism
```