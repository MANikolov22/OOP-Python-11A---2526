class Card:
    def pay(self, amount):
        return f"Paid {amount:.2f} with card"


class Cash:
    def pay(self, amount):
        return f"Paid {amount:.2f} in cash"


class Crypto:
    def pay(self, amount):
        return f"Paid {amount:.2f} in crypto"


def main():
    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        method = line[0].upper()
        amount = float(line[1])

        if method == "CARD":
            print(Card().pay(amount))
        elif method == "CASH":
            print(Cash().pay(amount))
        elif method == "CRYPTO":
            print(Crypto().pay(amount))
        else:
            print("Unknown payment method")


if __name__ == "__main__":
    main()