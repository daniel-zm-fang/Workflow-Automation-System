from .base import BaseWorkflow
from .base import BaseTrigger
from .base import BaseAction
import threading
import time


class PersistentWorkflow(BaseWorkflow):
    def __init__(
        self,
        name: str,
        trigger: BaseTrigger,
        actions: list[BaseAction],
        max_retries: int = 3,
        check_interval: float = 1.0,
    ):
        super().__init__(name, trigger, actions, max_retries)
        self.check_interval = check_interval
        self.running = False
        self.thread = None

    def run(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _run_loop(self):
        while self.running:
            if self.trigger.is_triggered():
                self._execute_workflow()
            time.sleep(self.check_interval)

    def _execute_workflow(self):
        data_store = {"trigger_data": self.trigger.get_trigger_data()}
        results = {"trigger_data": data_store["trigger_data"], "action_results": []}

        for action in self.actions:
            action_result = self._run_action_with_retry(action, data_store)
            results["action_results"].append(action_result)
            if action_result["status"] == "error":
                results["status"] = "error"
                print(f"Workflow {self.name} encountered an error: {results}")
                return
            
            # Add the action result to the data_store
            data_store[action.name] = action_result["result"]

        results["status"] = "success"
        print(f"Workflow {self.name} executed successfully: {results}")
