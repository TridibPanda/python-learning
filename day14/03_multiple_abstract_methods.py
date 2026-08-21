from abc import ABC, abstractmethod


# ABC makes Payment an abstract base class.
class Payment(ABC):
    # Every payment type must provide its own pay() implementation.
    @abstractmethod
    def pay(self):
        pass

    # Every payment type must provide its own refund() implementation.
    @abstractmethod
    def refund(self):
        pass

    # Concrete Method
    def check(self):
        print("Yes, I am your parent.")


# Concrete class that implements the abstract method.
class CreditCardPayment(Payment):
    def pay(self):
        print("Payment using Credit Card")

    def refund(self):
        print("Refund to Credit Card")


# Another concrete class that implements the abstract method.
class UPIPayment(Payment):
    def pay(self):
        print("Payment using UPI")

    def refund(self):
        print("Refund through UPI")

    def check(self):
        print("Yes, I am a child.")
        super().check()


credit_card = CreditCardPayment()
upi = UPIPayment()

# Same method call, different output: this demonstrates polymorphism.
credit_card.pay()  # Output: Payment using Credit Card
credit_card.refund()  # Output: Refund to Credit Card
upi.pay()  # Output: Payment using UPI
upi.refund()  # Output: Refund through UPI

credit_card.check()  # Output: Yes, I am your parent.
upi.check()
# Output:
# Yes, I am a child.
# Yes, I am your parent.
