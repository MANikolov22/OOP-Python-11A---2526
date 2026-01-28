from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class AddTextCommand(Command):
    # document е list със 1 елемент (mutable контейнер), напр. ["Hi"]
    def __init__(self, document: list[str], text_to_add: str) -> None:
        self.document = document
        self.text_to_add = text_to_add
        self._prev: str | None = None

    def execute(self) -> None:
        self._prev = self.document[0]
        self.document[0] = self.document[0] + self.text_to_add

    def undo(self) -> None:
        if self._prev is None:
            raise RuntimeError("Nothing to undo")
        self.document[0] = self._prev
