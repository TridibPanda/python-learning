# ============================================================
# SOLID Principles in Python
# ============================================================

# ============================================================
# S: Single Responsibility Principle
# ============================================================

# A class should have one responsibility, or one reason to change.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print("Saving user to database")

    def send_email(self):
        print("Sending email")

    def generate_report(self):
        print("Generating user report")


user = User("Tridib", "tridib@example.com")

user.save_to_database()  # Output: Saving user to database
user.send_email()  # Output: Sending email
user.generate_report()  # Output: Generating user report

"""
This User class is doing three different responsibilities:
User
 │
 ├── User data
 ├── Database operation
 ├── Email operation
 └── Report generation
 So there are multiple reasons for this class to change.
 For example:
 Database requirement changes
        ↓
User class changes

Email system changes
        ↓
User class changes

Report format changes
        ↓
User class changes
That's what SRP tries to avoid.
"""
# Better design
# Separate the responsibilities:


# What is the Single Responsibility Principle (SRP)?
# The Single Responsibility Principle (SRP) is one of the five SOLID principles of object-oriented design.
# It states that a class should have only one reason to change, meaning it should have only one responsibility or job.
# In other words, a class should focus on a single aspect of the functionality provided by the software, and it should encapsulate that aspect completely.
# By adhering to SRP, developers can create more maintainable, understandable, and flexible code.
# When a class has a single responsibility, it becomes easier to modify or extend that class without affecting other parts of the system,
# leading to better separation of concerns and reduced risk of introducing bugs when changes are made.


# Example of Single Responsibility Principle
class NewUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    def save(self, user):
        print("Saving user to database")


class EmailService:
    def send(self, user):
        print("Sending email")


class UserReport:
    def generate(self, user):
        print("Generating user report")


newuser = NewUser("Tridib", "tridib@example.com")

repository = UserRepository()
email_service = EmailService()
report = UserReport()

repository.save(newuser)  # Output: Saving user to database
email_service.send(newuser)  # Output: Sending email
report.generate(newuser)  # Output: Generating user report
"""
Now:

User
 ↓
Only responsible for user data


UserRepository
 ↓
Only database responsibility


EmailService
 ↓
Only email responsibility


UserReport
 ↓
Only report responsibility

This is much easier to maintain.
"""

# ============================================================
# O: Open/Closed Principle
# ============================================================


class Payment:
    def process(self, payment_type):
        if payment_type == "upi":
            print("Processing UPI payment")
        elif payment_type == "card":
            print("Processing Card payment")


"""
Now imagine tomorrow we add:
UPI
Card
PayPal
Crypto
Bank Transfer

We would keep modifying Payment.process():

if payment_type == "upi":
    ...
elif payment_type == "card":
    ...
elif payment_type == "paypal":
    ...
elif payment_type == "crypto":
    ...
    

This becomes difficult to maintain.

The Open/Closed Principle (OCP) says:
Software entities should be open for extension but closed for modification.

Open for extension
        ↓
We should be able to add new behavior


Closed for modification
        ↓
We should avoid repeatedly changing existing,
tested code to add that behavior.
"""

# A better design:

# what is the Open/Closed Principle (OCP)?
# The Open/Closed Principle (OCP) is one of the five SOLID principles of object-oriented design.
# It states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
# In other words, you should be able to add new functionality to a class or module without modifying its existing code.
# This principle promotes the use of abstraction, interfaces, and polymorphism to achieve flexibility and maintainability in software design.

# Example of Open/Closed Principle
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Processing UPI payment: ₹{amount}")


class Card(PaymentMethod):
    def pay(self, amount):
        print(f"Processing Card payment: ₹{amount}")


# Now suppose we need PayPal. We don't modify PaymentProcessor
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Processing PayPal payment: ₹{amount}")


# The existing PaymentProcessor remains unchanged when we add new payment methods. We can simply create a new class that implements the PaymentMethod interface, and the PaymentProcessor can work with it without any modifications.
class PaymentProcessor:
    def process(self, payment_method, amount):
        payment_method.pay(amount)


processor = PaymentProcessor()

processor.process(UPI(), 500)  # Output: Processing UPI payment: ₹500
processor.process(Card(), 1000)  # Output: Processing Card payment: ₹1000
processor.process(PayPal(), 1500)  # Output: Processing PayPal payment: ₹1500


# ============================================================
# L: Liskov Substitution Principle
# ============================================================


class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")


class Penguin(Bird):
    def fly(self):
        raise ValueError("Penguins cannot fly")


def make_bird_fly(bird: Bird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: Sparrow flying
# make_bird_fly(penguin)  # Output: raise ValueError: Penguins cannot fly

"""
The problem is:
Bird
 ├── Sparrow → can fly ✅
 └── Penguin → cannot fly ❌
 But Penguin inherits from Bird, and the parent says:

 def fly(self):
 
 So code using a Bird expects that fly() should work.

 When we substitute:
 make_bird_fly(penguin)
 the program breaks.

 That's what LSP is concerned with.
 LSP: Objects of a child class should be replaceable for objects of their parent class without breaking the correctness of the program.
"""

# A better design

# What is the Liskov Substitution Principle (LSP)?
# The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented design.
# It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
# In other words, if a class S is a subclass of class T, then objects of type T should be able to be replaced with objects of type S without altering the desirable properties of the program (e.g., correctness, task performed, etc.).
# This principle ensures that a subclass can stand in for its superclass without causing unexpected behavior or errors, promoting the use of polymorphism and enhancing code reusability and maintainability.

# What does "substitutable" mean in LSP?
# "substitutable" means that we can replace a parent class (base type) object with a child class (subclass) object anywhere in our code without breaking the program or causing unexpected errors.


# Example of Liskov Substitution Principle
class LSPBird:
    def eat(self):
        print("Eating")


class FlyingBird(LSPBird):
    def fly(self):
        print("Flying")


class LSPSparrow(FlyingBird):
    pass


class LSPPenguin(LSPBird):
    pass


def lsp_make_bird_fly(bird: FlyingBird):
    bird.fly()


lsp_make_bird_fly(LSPSparrow())  # Output: Flying

"""
Now:
Bird
 ├── FlyingBird
 │      └── Sparrow
 │
 └── Penguin
 Only birds that actually support flying inherit from FlyingBird.
"""

# ============================================================
# I: Interface Segregation Principle
# ============================================================


class Machine:
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Faxing document")


class SimplePrinter(Machine):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        raise NotImplementedError("SimplePrinter cannot scan")

    def fax_document(self):
        raise NotImplementedError("SimplePrinter cannot fax")


simple_printer = SimplePrinter()
simple_printer.print_document()  # Output: Printing document
# simple_printer.scan_document() # Output: raise NotImplementedError
# simple_printer.fax_document() # Output: raise NotImplementedError

"""
Problem: SimplePrinter only knows how to print, but because it inherits from Machine, it is forced to implement/support:
print_document() ✅
scan_document()  ❌
fax_document()   ❌

This violates Interface Segregation Principle (ISP).
Instead, separate the interfaces/capabilities:

"""

# A better design

# What is the Interface Segregation Principle (ISP)?
# The Interface Segregation Principle (ISP) is one of the five SOLID principles of object-oriented design.
# It states that no client should be forced to depend on methods it does not use.
# In other words, a class should not be required to implement interfaces or methods that it does not need or use. Instead, interfaces should be designed to be small and specific to the needs of the clients that use them.
# This principle promotes the creation of more focused and cohesive interfaces, leading to better maintainability, flexibility, and reduced coupling in software design.


# Example of Interface Segregation Principle
class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class Fax:
    def fax_document(self):
        print("Faxing document")


class BasicPrinter(Printer):
    pass


class MultiFunctionPrinter(Printer, Scanner, Fax):
    pass


basic_printer = BasicPrinter()
basic_printer.print_document()  # Output: Printing document

multi_printer = MultiFunctionPrinter()
multi_printer.print_document()  # Output: Printing document
multi_printer.scan_document()  # Output: Scanning document
multi_printer.fax_document()  # Output: Faxing document

"""
Now:
Printer
   ↓
SimplePrinter
   → print ✅


Printer + Scanner + Fax
          ↓
MultiFunctionPrinter
   → print ✅
   → scan  ✅
   → fax   ✅

The key idea:
Clients should not be forced to depend on methods they do not use.
In simple words: don't create one huge interface containing everything; split it into smaller, focused interfaces.

"""

# ============================================================
# D: Dependency Inversion Principle
# ============================================================


class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL")


class UserService:
    def __init__(self):
        self.database = MySQLDatabase()

    def save_user(self, user):
        self.database.save(user)


service = UserService()
service.save_user("Tridib")  # Output: Saving Tridib to MySQL

"""
At first this looks fine.
But there is a problem:
UserService
     ↓
MySQLDatabase

UserService is directly dependent on a concrete database implementation.
Now imagine tomorrow we want MongoDB:

class MongoDatabase:
    def save(self, data):
        print(f"Saving {data} to MongoDB")

We would have to modify UserService:

class UserService:
    def __init__(self):
        self.database = MongoDatabase()
That's tight coupling.

"""
# A better design
# What is the Dependency Inversion Principle (DIP)?
# The Dependency Inversion Principle (DIP) is one of the five SOLID principles of object-oriented design.
# It states that high-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces or abstract classes).
# Additionally, abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
# In other words, the principle encourages the decoupling of software modules by introducing abstractions that allow high-level components to remain independent of low-level implementation details.
# This promotes flexibility, maintainability, and testability in software design, as changes to low-level modules do not directly affect high-level modules.

# Example of Dependency Inversion Principle
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class SQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL")


class MongoDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")


class UserTableService:
    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)


# Now we decide which database to provide:

mysql = SQLDatabase()
service = UserTableService(mysql)

service.save_user("Tridib")  # Output : Saving Tridib to MySQL

# Or

mongo = MongoDatabase()
service = UserTableService(mongo)

service.save_user("Tridib")  # Output: Saving Tridib to MongoDB

"""
UserService doesn't need to know whether the database is MySQL or MongoDB.
The relationship becomes:
             Database
            /        \
           /          \
      MySQL           MongoDB
         |             /
         |            /
          UserService

The important part is:
UserService
     ↓
 Database abstraction
     ↑
     |
MySQL / MongoDB

DIP : High-level modules should not depend on low-level modules. Both should depend on abstractions.
And:
Abstractions should not depend on details. Details should depend on abstractions.
In our example:
High-level:
UserService

Low-level:
MySQLDatabase
MongoDatabase

Abstraction:
Database

Instead of:
UserService → MySQLDatabase
we have:
UserService → Database ← MySQLDatabase
                         ← MongoDatabase

This makes the code easier to change and test.
And notice something important: this is also where Dependency Injection comes in.
We don't create the database inside UserService anymore:
self.database = MySQLDatabase()

Instead, we inject it:
def __init__(self, database: Database):
    self.database = database
"""
