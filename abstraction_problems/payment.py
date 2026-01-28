from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def fee(self, amount: float) -> float:
        pass

    @abstractmethod
    def pay(self, amount: float) -> tuple[float, str]:
        pass


class CardProcessor(PaymentProcessor):
    def fee(self, amount: float) -> float:
        return amount * 0.025

    def pay(self, amount: float) -> tuple[float, str]:
        f = self.fee(amount)
        total = amount + f
        return total, f"Card payment: amount={amount:.2f}, fee={f:.2f}, total={total:.2f}"


class CryptoProcessor(PaymentProcessor):
    def fee(self, amount: float) -> float:
        return amount * 0.01 + 0.50

    def pay(self, amount: float) -> tuple[float, str]:
        f = self.fee(amount)
        total = amount + f
        return total, f"Crypto payment: amount={amount:.2f}, fee={f:.2f}, total={total:.2f}"
