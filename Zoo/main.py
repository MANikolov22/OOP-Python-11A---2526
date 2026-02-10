from Zoo import Zoo
from Lion import Lion
from Cow import Cow
from Bear import Bear


def main():
    zoo = Zoo()

    simba = Lion("Симба", 5)
    marta = Cow("Марта", 7)
    baloo = Bear("Балу", 12)

    zoo.add_animal(simba)
    zoo.add_animal(marta)
    zoo.add_animal(baloo)

    zoo.list_animals()
    zoo.feed_animals()


if __name__ == "__main__":
    main()