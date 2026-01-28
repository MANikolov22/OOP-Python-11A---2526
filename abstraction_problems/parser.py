from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self, text: str) -> dict[str, str]:
        pass


class KeyValueParser(Parser):
    # формат: "a=1;b=2"
    def parse(self, text: str) -> dict[str, str]:
        result: dict[str, str] = {}
        text = text.strip()
        if not text:
            return result

        parts = [p for p in text.split(";") if p.strip()]
        for part in parts:
            if "=" not in part:
                raise ValueError(f"Invalid pair (missing '='): {part}")
            k, v = part.split("=", 1)
            result[k.strip()] = v.strip()

        return result
