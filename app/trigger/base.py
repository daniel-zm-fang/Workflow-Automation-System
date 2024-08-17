from abc import ABC, abstractmethod
from typing import Any


class BaseTrigger(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def is_triggered(self) -> bool:
        """Check if the trigger condition is met."""
        pass

    @abstractmethod
    def get_trigger_data(self) -> dict[str, Any]:
        """Return the data associated with the trigger event."""
        pass
