from abc import ABC, abstractmethod


class Step(ABC):
    @abstractmethod
    def run(self, data: str) -> str:
        pass


class LowercaseStep(Step):
    def run(self, data: str) -> str:
        return data.lower()


class StripStep(Step):
    def run(self, data: str) -> str:
        return data.strip()


def run_pipeline(steps: list[Step], text: str) -> str:
    data = text
    for step in steps:
        data = step.run(data)
    return data
