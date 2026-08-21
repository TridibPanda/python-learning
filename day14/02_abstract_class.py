from abc import ABC, abstractmethod


# ABC makes Payment an abstract base class.
class Payment(ABC):
    # Every payment type must provide its own pay() implementation.
    @abstractmethod
    def pay(self):
        pass


# Concrete class that implements the abstract pay() method.
class CreditCardPayment(Payment):
    def pay(self):
        print("Payment using Credit Card")


# Another concrete class with its own pay() behavior.
class UPIPayment(Payment):
    def pay(self):
        print("Payment using UPI")


# Objects of different payment classes use the same method interface.
credit_card = CreditCardPayment()
upi = UPIPayment()

# Same method call, different output: this demonstrates polymorphism.
credit_card.pay()  # Output: Payment using Credit Card
upi.pay()  # Output: Payment using UPI
