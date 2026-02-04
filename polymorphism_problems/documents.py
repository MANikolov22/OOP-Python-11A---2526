class PDF:
    def export(self, text):
        return f"[PDF] {text} [/PDF]"


class HTML:
    def export(self, text):
        return f"<p>{text}</p>"


class TXT:
    def export(self, text):
        return text


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split(" ", 1)
        fmt = line[0].upper()
        content = line[1] if len(line) > 1 else ""

        if fmt == "PDF":
            print(PDF().export(content))
        elif fmt == "HTML":
            print(HTML().export(content))
        elif fmt == "TXT":
            print(TXT().export(content))
        else:
            print("Unknown format")


if __name__ == "__main__":
    main()