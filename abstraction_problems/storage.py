from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):
    @abstractmethod
    def save(self, key: str, value: Any) -> None:
        pass

    @abstractmethod
    def load(self, key: str) -> Any:
        pass


class MemoryStorage(Storage):
    def __init__(self) -> None:
        self._data: dict[str, Any] = {}

    def save(self, key: str, value: Any) -> None:
        self._data[key] = value

    def load(self, key: str) -> Any:
        return self._data.get(key)
