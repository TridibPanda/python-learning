from abc import ABC, abstractmethod


# ABC makes Payment an abstract base class.
class Payment(ABC):
    # Constructor method
    def __init__(self, amount):
        self.amount = amount

    # Every payment type must provide its own pay() implementation.
    @abstractmethod
    def pay(self):
        pass

    # Concrete Method
    def show_amount(self):
        print(f"Amount: {self.amount}")


# Concrete class that implements the abstract method.
class UPIPayment(Payment):
    # Constructor method
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    # abstract method
    def pay(self):
        print(f"Payment of {self.amount} using UPI Id {self.upi_id}")


payment = UPIPayment(500, "tridib@upi")
payment.show_amount()  # Output: Amount: 500
payment.pay()  # Output: Payment of 500 using UPI Id tridib@upi

print(payment.upi_id)  # Output: tridib@upi
