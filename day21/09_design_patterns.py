# Design Pattern

# ============================================================
# Factory Pattern
# ============================================================


class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


class PushNotification:
    def send(self, message):
        print(f"Push: {message}")


# Without a Factory, we might write:

notification_type = "email"

if notification_type == "email":
    notification = EmailNotification()
elif notification_type == "sms":
    notification = SMSNotification()
elif notification_type == "push":
    notification = PushNotification()

notification.send("Hello Tridib")  # Output: Email: Hello Tridib
# The problem is that the code responsible for using the notification also needs to know which concrete class to create.


# Factory separates object creation:
class NotificationFactory:
    @staticmethod
    def create(notification_type):
        if notification_type == "email":
            return EmailNotification()

        if notification_type == "sms":
            return SMSNotification()

        if notification_type == "push":
            return PushNotification()

        raise ValueError("Unknown notification type")


notification = NotificationFactory.create("email")
notification.send("Hello Tridib")  # Output: Email: Hello Tridib

# Factory Pattern centralizes object creation so the caller doesn't need to directly decide which concrete object to instantiate.

# ============================================================
# Strategy Pattern
# ============================================================


class UPIPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


"""
Instead of putting everything inside:
if payment_type == "upi":
    ...
elif payment_type == "card":
    ...
"""


# we can inject the strategy:
class PaymentService:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)


upi = UPIPayment()
service = PaymentService(upi)

service.pay(500)  # Output: Paid ₹500 using UPI

card = CardPayment()
service = PaymentService(card)

service.pay(500)  # Output: Paid ₹500 using Card
"""
The PaymentService doesn't need to know how UPI or Card payment works.
It simply says:
"I have a payment strategy.
Ask that strategy to pay."
That's Strategy Pattern.
"""

# ============================================================
# Observer Pattern
# ============================================================
"""
One object changes, and multiple other objects need to know about that change.

For example:
Order Status Changed
        ↓
       Order
      /  |   \
     ↓   ↓    ↓
 Email  SMS  Push
 The Order doesn't need to directly contain all notification logic.
 Observers subscribe to the order:
"""


class Order:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class EmailObserver:
    def update(self, message):
        print(f"Email notification: {message}")


class SMSObserver:
    def update(self, message):
        print(f"SMS notification: {message}")


order = Order()
order.subscribe(EmailObserver())
order.subscribe(SMSObserver())

order.notify("Order shipped")
# Output: Email notification: Order shipped
# Output: SMS notification: Order shipped
# The important idea: One object publishes an event, and subscribed objects react to it.

# ============================================================
# Singleton Pattern
# ============================================================


# A Singleton means: A class is designed so that only one instance of it is shared.
# For example, imagine a configuration manager:
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


config1 = Config()
config2 = Config()
print(config1 is config2)  # Output: True

"""
Both variables point to the same object:
config1 ──┐
          ↓
       Config object
          ↑
config2 ──┘
Without Singleton:
config1 = Config()
config2 = Config()
would normally create two separate objects.
With Singleton, the second creation returns the already-existing instance.

Why Singleton can be useful

Suppose you have some shared application-wide configuration:
class AppConfig:
    database_url = "..."
    api_key = "..."

Other possible examples include:

application configuration
certain resource managers
a shared registry

But Singleton has a downside: it introduces global/shared state.

That can make code harder to test because different parts of the application are secretly using the same object.

Why Dependency Injection is often better
Suppose we need a configuration object.

Singleton approach

The class gets the global object itself:
"""
# Dependency Injection approach


class AppConfig:
    database_url = "..."
    api_key = "..."


class UserService:
    def __init__(self, config):
        self.config = config


config = AppConfig()

service = UserService(config)

"""
Now:
Application
    |
    | gives dependency
    ↓
UserService
    |
    ↓
config

This is cleaner for testing.

For example, in a test we can provide a fake configuration:
fake_config = FakeConfig()

service = UserService(fake_config)

We don't have to modify UserService.

The key difference

Singleton
UserService → creates/accesses shared dependency itself

Dependency Injection
UserService ← dependency supplied from outside

So DI doesn't necessarily mean there can only be one instance.
You can inject: config1 , config2 or even a fake/mock object during testing.

That's a major reason DI is generally more flexible and test-friendly than relying on Singleton/global state.
"""
