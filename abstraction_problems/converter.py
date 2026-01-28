from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def convert(self, value: float) -> float:
        pass


class CelsiusToFahrenheit(Converter):
    def convert(self, value: float) -> float:
        return value * 9 / 5 + 32


class KmToMiles(Converter):
    def convert(self, value: float) -> float:
        return value * 0.621371
