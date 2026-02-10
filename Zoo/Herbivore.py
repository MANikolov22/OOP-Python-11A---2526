from abc import ABC


class Herbivore(ABC):
    def graze(self) -> str:
        return f"{self.__class__.__name__} {self.name} пасе спокойно трева."