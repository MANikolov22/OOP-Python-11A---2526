from abc import ABC


class Carnivore(ABC):
    def hunt(self) -> str:
        return f"{self.__class__.__name__} {self.name} ловува агресивно и тихо се промъква към плячката."