class Payment:
    def pay(self):
        raise NotImplementedError


class CreditCardPayment(Payment):
    def pay(self):
        print("Payment using Credit Card")


class UPIPayment(Payment):
    def pay(self):
        print("Payment using UPI")


credit_card = CreditCardPayment()
upi = UPIPayment()

credit_card.pay()  # Output: Payment using Credit Card
upi.pay()  # Output: Payment using UPI
