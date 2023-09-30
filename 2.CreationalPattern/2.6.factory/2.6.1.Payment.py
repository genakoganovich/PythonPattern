from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Making a credit card payment of {amount} dollars.")


class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"Making a PayPal payment of {amount} dollars.")


class PaymentFactory:
    def create_payment(self, method):
        if method == "creditcard":
            return CreditCardPayment()
        elif method == "paypal":
            return PaypalPayment()
        else:
            raise ValueError(f"Invalid payment method {method}.")


if __name__ == "__main__":
    factory = PaymentFactory()
    payment = factory.create_payment("creditcard")
    payment.pay(100)
    payment = factory.create_payment("paypal")
    payment.pay(50)
