from abc import ABC, abstractmethod
from typing import Any


class BaseAction(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, data_store: dict[str, Any]) -> dict[str, Any]:
        pass
