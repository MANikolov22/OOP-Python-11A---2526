from typing import List
from Animal import Animal


class Zoo:
    def __init__(self):
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Добавено животно: {animal.name} ({animal.__class__.__name__})")
        else:
            print("Може да се добавят само обекти от тип Animal!")

    def list_animals(self) -> None:
        if not self.animals:
            print("Зоопаркът е празен.")
            return

        print("\nЖивотни в зоопарка:")
        print("-" * 50)
        for animal in self.animals:
            print(animal)
        print("-" * 50)

    def feed_animals(self) -> None:
        if not self.animals:
            print("Няма животни за хранене.")
            return

        print("\nХранене на животните:")
        print("-" * 50)

        for animal in self.animals:
            print(f"→ {animal.name} ({animal.__class__.__name__}):")


            from Carnivore import Carnivore
            from Herbivore import Herbivore

            if isinstance(animal, Carnivore):
                print("  " + animal.hunt())

            if isinstance(animal, Herbivore):
                print("  " + animal.graze())

            print()