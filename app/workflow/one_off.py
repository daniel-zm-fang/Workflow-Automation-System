from .base import BaseWorkflow


class OneOffWorkflow(BaseWorkflow):
    def run(self):
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
