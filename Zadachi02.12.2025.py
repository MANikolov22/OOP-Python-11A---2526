
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # списък от оценки

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозирани {amount} лв. Нов баланс: {self.balance} лв.")
        else:
            print("Сумата за депозит трябва да е положителна!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатъчно средства!")
        elif amount <= 0:
            print("Сумата за теглене трябва да е положителна!")
        else:
            self.balance -= amount
            print(f"Изтеглени {amount} лв. Оставащ баланс: {self.balance} лв.")

    def get_balance(self):
        return self.balance



class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15



class Car:
    def __init__(self, model, fuel_consumption_l_per_100km, fuel_in_tank):
        self.model = model
        self.fuel_consumption = fuel_consumption_l_per_100km  # литри на 100 км
        self.fuel_in_tank = fuel_in_tank  # литри

    def can_travel(self, distance_km):
        needed_fuel = (self.fuel_consumption / 100) * distance_km
        if needed_fuel <= self.fuel_in_tank:
            return True
        else:
            return False



if __name__ == "__main__":
    print("=== 1. Rectangle ===")
    rect = Rectangle(5, 3)
    print(f"Лице: {rect.area()}")
    print(f"Периметър: {rect.perimeter()}")
    print()

    print("=== 2. Student ===")
    student = Student("Иван Петров", [4, 5, 6, 5, 5])
    print(f"Име: {student.name}")
    print(f"Среден успех: {student.average():.2f}")
    print()

    print("=== 3. BankAccount ===")
    account = BankAccount("Мария Иванова", 1000)
    print(f"Начално салдо: {account.get_balance()} лв.")
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # няма да мине
    account.withdraw(1300)
    print()

    print("=== 4. TemperatureConverter ===")
    temp = TemperatureConverter(25)
    print(f"25°C = {temp.to_fahrenheit():.1f}°F")
    print(f"25°C = {temp.to_kelvin():.1f}K")
    print()

    print("=== 5. Car ===")
    car = Car("Toyota Corolla", 6.5, 35)  # 6.5 л/100 км, 35 литра в резервоара
    distance = 500
    if car.can_travel(distance):
        print(f"{car.model} може да измине {distance} км с текущото гориво.")
    else:
        needed = (car.fuel_consumption / 100) * distance
        print(f"{car.model} НЕ може да измине {distance} км.")
        print(f"   Нужно гориво: {needed:.1f} л, налично: {car.fuel_in_tank} л")