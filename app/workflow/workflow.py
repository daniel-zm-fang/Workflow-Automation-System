from typing import Any
import time
from app.trigger.base import BaseTrigger
from app.action.base import BaseAction


class Workflow:
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

    def run(self) -> dict[str, Any]:
        if not self.trigger.is_triggered():
            return {"status": "not_triggered"}

        data_store = self.trigger.get_trigger_data()
        results = {"trigger_data": data_store, "action_results": []}

        for action in self.actions:
            action_result = self._run_action_with_retry(action, data_store)
            results["action_results"].append(action_result)
            if action_result["status"] == "error":
                results["status"] = "error"
                return results

        results["status"] = "success"
        return results

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
                    return {"name": action.name, "status": "error", "error": str(e)}
                time.sleep(2**attempt)  # Exponential backoff

        return {"name": action.name, "status": "error", "error": "Max retries reached"}
