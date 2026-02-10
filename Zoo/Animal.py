from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.age} години, звук: {self.make_sound()}"