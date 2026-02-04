from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        shape = line[0].upper()

        if shape == "CIRCLE":
            r = float(line[1])
            print(f"{Circle(r).area():.2f}")
        elif shape == "RECT":
            w, h = float(line[1]), float(line[2])
            print(f"{Rectangle(w, h).area():.2f}")
        else:
            print("Unknown shape")


if __name__ == "__main__":
    main()