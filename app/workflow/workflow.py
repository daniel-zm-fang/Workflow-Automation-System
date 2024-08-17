from typing import Any
from app.trigger.base import BaseTrigger
from app.action.base import BaseAction


class Workflow:
    def __init__(self, name: str, trigger: BaseTrigger, actions: list[BaseAction]):
        self.name = name
        self.trigger = trigger
        self.actions = actions
        self.data_store: dict[str, Any] = {}

    def run(self) -> dict[str, Any]:
        if not self.trigger.is_triggered():
            return {"status": "not_triggered"}

        self.data_store["trigger"] = self.trigger.get_trigger_data()

        for i, action in enumerate(self.actions):
            try:
                result = action.execute(self.data_store)
                self.data_store[f"action_{i}"] = result
            except Exception as e:
                return {"status": "error", "action": action.name, "error": str(e)}

        return {"status": "completed", "result": self.data_store}
