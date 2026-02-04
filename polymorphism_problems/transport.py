class Car:
    def cost(self, km):
        return km * 0.50


class Bus:
    def cost(self, km):
        return km * 0.20


class Bike:
    def cost(self, km):
        return 0.0


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        vehicle = line[0].upper()
        km = float(line[1])

        if vehicle == "CAR":
            print(f"{Car().cost(km):.2f}")
        elif vehicle == "BUS":
            print(f"{Bus().cost(km):.2f}")
        elif vehicle == "BIKE":
            print(f"{Bike().cost(km):.2f}")
        else:
            print("Unknown vehicle")


if __name__ == "__main__":
    main()