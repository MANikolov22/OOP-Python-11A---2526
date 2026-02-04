class FullTime:
    def salary(self):
        return 2000.0


class PartTime:
    def __init__(self, hours):
        self.hours = hours

    def salary(self):
        return self.hours * 15


class Intern:
    def salary(self):
        return 500.0


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        typ = line[0].upper()

        if typ == "FULLTIME":
            print(f"{FullTime().salary():.2f}")
        elif typ == "PARTTIME":
            hours = float(line[1])
            print(f"{PartTime(hours).salary():.2f}")
        elif typ == "INTERN":
            print(f"{Intern().salary():.2f}")
        else:
            print("Unknown employee type")


if __name__ == "__main__":
    main()