from .base import BaseTrigger
from typing import Any
from datetime import datetime, timedelta


class ScheduledTrigger(BaseTrigger):
    def __init__(self, name: str, schedule: timedelta):
        super().__init__(name)
        self.schedule = schedule
        self.last_run = datetime.now() - schedule

    def is_triggered(self) -> bool:
        now = datetime.now()
        if now - self.last_run >= self.schedule:
            self.last_run = now
            return True
        return False

    def get_trigger_data(self) -> dict[str, Any]:
        return {"scheduled_time": self.last_run.isoformat()}
