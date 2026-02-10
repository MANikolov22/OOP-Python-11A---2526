from Animal import Animal
from Carnivore import Carnivore


class Lion(Carnivore, Animal):
    def make_sound(self) -> str:
        return "Рррр!"

    def hunt(self) -> str:
        return f"Лъвът {self.name} издава мощно ръмжене и се хвърля в атака!"