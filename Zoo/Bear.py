from Animal import Animal
from Omnivore import Omnivore


class Bear(Omnivore, Animal):
    def make_sound(self) -> str:
        return "Ръммм!"