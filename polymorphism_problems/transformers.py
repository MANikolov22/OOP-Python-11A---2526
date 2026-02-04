class Upper:
    def transform(self, text):
        return text.upper()


class Lower:
    def transform(self, text):
        return text.lower()


class Reverse:
    def transform(self, text):
        return text[::-1]


class VowelsToStar:
    def transform(self, text):
        vowels = set("aeiouAEIOU")
        return "".join("*" if c in vowels else c for c in text)


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split(" ", 1)
        cmd = line[0].upper()
        text = line[1] if len(line) > 1 else ""

        if cmd == "UPPER" or cmd == "UP":
            print(Upper().transform(text))
        elif cmd == "LOWER":
            print(Lower().transform(text))
        elif cmd == "REVERSE":
            print(Reverse().transform(text))
        elif cmd == "VOWELSTOSTAR" or cmd == "VOWELS":
            print(VowelsToStar().transform(text))
        else:
            print("Unknown transformer")


if __name__ == "__main__":
    main()