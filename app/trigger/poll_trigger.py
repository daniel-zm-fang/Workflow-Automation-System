from .base import BaseTrigger
from typing import Any, Callable
import time
from datetime import datetime


class PollTrigger(BaseTrigger):
    def __init__(
        self, name: str, poll_interval: int, condition_check: Callable[[], bool]
    ):
        super().__init__(name)
        self.poll_interval = poll_interval
        self.condition_check = condition_check
        self.last_poll = time.time() - poll_interval

    def is_triggered(self) -> bool:
        now = time.time()
        if now - self.last_poll >= self.poll_interval:
            self.last_poll = now
            return self.condition_check()
        return False

    def get_trigger_data(self) -> dict[str, Any]:
        return {"poll_time": datetime.fromtimestamp(self.last_poll).isoformat()}
