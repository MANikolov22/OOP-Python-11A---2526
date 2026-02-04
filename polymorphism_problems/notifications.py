class Email:
    def send(self, msg):
        return f"EMAIL: {msg}"


class SMS:
    def send(self, msg):
        return f"SMS: {msg}"


class Push:
    def send(self, msg):
        return f"PUSH: {msg}"


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split(" ", 1)
        typ = line[0].upper()
        message = line[1] if len(line) > 1 else ""

        if typ == "EMAIL":
            print(Email().send(message))
        elif typ == "SMS":
            print(SMS().send(message))
        elif typ == "PUSH":
            print(Push().send(message))
        else:
            print("Unknown notification type")


if __name__ == "__main__":
    main()