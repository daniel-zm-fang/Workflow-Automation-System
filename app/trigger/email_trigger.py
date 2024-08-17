from .base import BaseTrigger
from typing import Any


class EmailTrigger(BaseTrigger):
    def __init__(self, name: str, imap_server: str, email_address: str, password: str):
        super().__init__(name)
        self.imap_server = imap_server
        self.email_address = email_address
        self.password = password

    def is_triggered(self) -> bool:
        # Mock implementation
        return True

    def get_trigger_data(self) -> dict[str, Any]:
        # Mock implementation
        return {
            "from": "sender@example.com",
            "subject": "Insurance Application",
            "attachments": [
                {"filename": "application.pdf", "content": "mocked pdf content"}
            ],
            "content": "Hi,\n\nI would like to apply for an insurance policy.",
        }
