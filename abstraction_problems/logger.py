from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> str:
        return f"[Console] {message}"


class FileLogger(Logger):
    def __init__(self, filename: str = "app.log") -> None:
        self.filename = filename

    def log(self, message: str) -> str:
        return f"[File:{self.filename}] {message}"
