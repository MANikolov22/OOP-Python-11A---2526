from Animal import Animal
from Herbivore import Herbivore


class Cow(Herbivore, Animal):
    def make_sound(self) -> str:
        return "Муууу!"

    def graze(self) -> str:
        return f"Кравата {self.name} кротко дъвче трева и преживя."