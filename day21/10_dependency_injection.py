# The problem — tight coupling


class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL")


class UserService:
    def __init__(self):
        self.database = MySQLDatabase()

    def create_user(self, name):
        self.database.save(name)


service = UserService()
service.create_user("Tridib")  # Output: Saving Tridib to MySQL
# The problem is here — UserService is tightly coupled to MySQLDatabase
# If we want to change the database to MongoDB, we would have to modify the UserService class.

# Constructor Injection
# Instead of creating the database instance inside the UserService class, we can pass it as a parameter to the constructor. This way, we can easily switch to a different database implementation without modifying the UserService class.


class UserServiceCI:
    # Constructor Injection
    def __init__(self, database):
        self.database = database

    def create_user(self, name):
        self.database.save(name)


class MongoDatabase:
    def save(self, data):
        print(f"Saving {data} to MongoDB")


# Now, we can create instances of UserServiceCI with different database implementations without modifying the UserServiceCI class itself.
mysql = MySQLDatabase()

service = UserServiceCI(mysql)
service.create_user("Tridib")  # Output: Saving Tridib to MySQL

# Now, we can easily switch to MongoDB without modifying the UserServiceCI class.
mongo = MongoDatabase()

service = UserServiceCI(mongo)
service.create_user("Tridib")  # Output: Saving Tridib to MongoDB

# This is Dependency Injection.
# What is Dependency Injection?
# Dependency Injection is a design pattern that allows us to remove the hard-coded dependencies between classes and make our code more flexible and easier to maintain.
# It allows us to inject the dependencies (in this case, the database) into a class rather than creating them inside the class. This way, we can easily switch to different implementations of the dependencies without modifying the class itself.

# Using an abstraction for the database dependency
# We can further improve our code by using an abstraction for the database dependency. This way, we can define a common interface for all database implementations, and the UserService class can depend on that interface rather than a specific implementation. This will make our code even more flexible and easier to maintain.

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDB(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL")


class MongoDB(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")


class UserServiceDIP:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, name):
        self.database.save(name)


mysql = MySQLDB()
service = UserServiceDIP(mysql)

service.create_user("Tridib")  # Output: Saving Tridib to MySQL

mongo = MongoDB()
service = UserServiceDIP(mongo)

service.create_user("Tridib")  # Output: Saving Tridib to MongoDB

"""
The architecture becomes:
                 Database
                /        \
               /          \
      MySQLDatabase    MongoDatabase
               |          /
               |         /
                 UserService
More precisely, UserServiceDIP depends on the abstraction, while the concrete database implementations depend on that abstraction.
"""

# Dependency Injection and testing


# We can also use Dependency Injection to make our code more testable. By injecting a fake database implementation into the UserService class, we can easily test the create_user method without actually saving data to a real database.
class FakeDatabase:
    def save(self, data):
        print(f"Fake save: {data}")


fake_db = FakeDatabase()

service = UserServiceCI(fake_db)

service.create_user("Test User")  # Output: Fake save: Test User

# Dependency Inversion Principle (DIP) → What should the dependency relationship look like?
# Dependency Injection (DI)  → How do we provide the dependency?
