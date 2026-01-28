from abc import ABC, abstractmethod
from typing import Any
import json
import csv
import io


class DataExporter(ABC):
    @abstractmethod
    def export(self, rows: list[dict[str, Any]]) -> str:
        pass


class JsonExporter(DataExporter):
    def export(self, rows: list[dict[str, Any]]) -> str:
        return json.dumps(rows, ensure_ascii=False, indent=2)


class CsvExporter(DataExporter):
    # CSV само от ключовете на първия ред
    def export(self, rows: list[dict[str, Any]]) -> str:
        if not rows:
            return ""

        fieldnames = list(rows[0].keys())
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        return buffer.getvalue()
