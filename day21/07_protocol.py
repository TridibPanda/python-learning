from typing import Protocol


# What is a Protocol?
# Ans: A Protocol is a way to define a set of methods and properties that a class must implement, without requiring the class to inherit from a specific base class. It allows for structural subtyping, meaning that if a class has the required methods and properties, it can be considered a subtype of the Protocol, even if it doesn't explicitly inherit from it.
class PaymentProcessor(Protocol):
    def pay(self, amount: float) -> None: ...

    # The ... is called an Ellipsis. ... -> No implementation is being provided here.


class UPI:
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using UPI")


class Card:
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using Card")


class Cash:
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} using Cash")


#  The object should have the structure described by PaymentProcessor. This is known as structural subtyping or duck typing.
def process_payment(processor: PaymentProcessor, amount: float) -> None:
    processor.pay(amount)


upi = UPI()
card = Card()
cash = Cash()

process_payment(upi, 500)  # Output: Paid ₹500 using UPI
process_payment(card, 1000)  # Output: Paid ₹1000 using Card
process_payment(cash, 300)  # Output: Paid ₹300 using Cash

"""
Duck typing
     ↓
"What can this object do?"


Protocol
     ↓
"What should this object provide?"
     +
"Tell the type checker/IDE about that requirement"

Protocol = structural typing.
"""
