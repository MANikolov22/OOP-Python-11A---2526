class Warrior:
    def attack(self):
        return 30


class Mage:
    def attack(self):
        return 25


class Archer:
    def attack(self):
        return 20


def main():
    total = 0
    n = int(input())
    for _ in range(n):
        char = input().strip().upper()

        if char == "WARRIOR":
            dmg = Warrior().attack()
        elif char == "MAGE":
            dmg = Mage().attack()
        elif char == "ARCHER":
            dmg = Archer().attack()
        else:
            dmg = 0
            print("Unknown character")

        print(dmg)
        total += dmg

    print(f"Total attack: {total}")


if __name__ == "__main__":
    main()