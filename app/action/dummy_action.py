from .base import BaseAction
from typing import Any


class DummyAction(BaseAction):
    def execute(self, data_store: dict[str, Any]) -> dict[str, Any]:
        print("Executing Dummy Action")
        return {"message": "Dummy action executed successfully"}
