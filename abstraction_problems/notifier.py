from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> str:
        pass


class EmailNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"[Email -> {to}] {message}"


class SMSNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"[SMS -> {to}] {message}"
