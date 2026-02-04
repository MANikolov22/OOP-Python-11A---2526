from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CardPayment(PaymentMethod):
    def __init__(self, last4: str):
        self.last4 = last4

    def pay(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Сумата трябва да бъде положително число")
        return f"Paid {amount:.2f} by card ****{self.last4}"


class CashOnDelivery(PaymentMethod):
    def pay(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Сумата трябва да бъде положително число")
        return f"Paid {amount:.2f} cash on delivery"
