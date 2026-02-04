class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


class Cow:
    def speak(self):
        return "Moo"


def main():
    n = int(input())
    for _ in range(n):
        animal_type = input().strip().upper()

        if animal_type == "DOG":
            print(Dog().speak())
        elif animal_type == "CAT":
            print(Cat().speak())
        elif animal_type == "COW":
            print(Cow().speak())
        else:
            print("Unknown animal")


if __name__ == "__main__":
    main()