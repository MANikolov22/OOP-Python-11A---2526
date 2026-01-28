from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any


@dataclass(frozen=True)
class CacheEntry:
    value: Any
    expires_at: datetime | None


class Cache(ABC):
    @abstractmethod
    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        pass

    @abstractmethod
    def get(self, key: str) -> Any:
        pass


class SimpleCache(Cache):
    def __init__(self) -> None:
        self._data: dict[str, CacheEntry] = {}

    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        expires_at = None
        if ttl_seconds is not None:
            expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
        self._data[key] = CacheEntry(value=value, expires_at=expires_at)

    def get(self, key: str) -> Any:
        entry = self._data.get(key)
        if entry is None:
            return None

        if entry.expires_at is not None and datetime.utcnow() >= entry.expires_at:
            del self._data[key]
            return None

        return entry.value
