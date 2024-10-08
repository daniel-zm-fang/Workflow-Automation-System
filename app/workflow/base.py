from abc import ABC, abstractmethod
from typing import Any
from app.trigger.base import BaseTrigger
from app.action.base import BaseAction
import time


class BaseWorkflow(ABC):
    def __init__(
        self,
        name: str,
        trigger: BaseTrigger,
        actions: list[BaseAction],
        max_retries: int = 3,
    ):
        self.name = name
        self.trigger = trigger
        self.actions = actions
        self.max_retries = max_retries

    @abstractmethod
    def run(self):
        pass

    def _run_action_with_retry(
        self, action: BaseAction, data_store: dict[str, Any]
    ) -> dict[str, Any]:
        for attempt in range(self.max_retries):
            try:
                action_result = action.execute(data_store)
                return {
                    "name": action.name,
                    "status": "success",
                    "result": action_result,
                }
            except Exception as e:
                if attempt == self.max_retries - 1:
                    return {
                        "name": action.name,
                        "status": "error",
                        "error": e.__repr__(),
                    }
                time.sleep(2**attempt)  # Exponential backoff

        return {"name": action.name, "status": "error", "error": "Max retries reached"}
