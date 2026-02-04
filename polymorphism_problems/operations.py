class Add:
    def apply(self, a, b):
        return a + b


class Sub:
    def apply(self, a, b):
        return a - b


class Mul:
    def apply(self, a, b):
        return a * b


class Div:
    def apply(self, a, b):
        if b == 0:
            return "ERROR"
        return a / b


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        op = line[0].upper()
        try:
            x = float(line[1])
            y = float(line[2])
        except:
            print("Invalid input")
            continue

        if op == "ADD":
            print(Add().apply(x, y))
        elif op == "SUB":
            print(Sub().apply(x, y))
        elif op == "MUL":
            print(Mul().apply(x, y))
        elif op == "DIV":
            res = Div().apply(x, y)
            if isinstance(res, str):
                print(res)
            else:
                print(f"{res:.2f}" if res != int(res) else int(res))
        else:
            print("Unknown operation")


if __name__ == "__main__":
    main()