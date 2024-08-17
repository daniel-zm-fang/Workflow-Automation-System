from .base import BaseAction
from typing import Any


class SendEmailAction(BaseAction):
    def __init__(
        self, name: str, smtp_server: str, sender_email: str, sender_password: str
    ):
        super().__init__(name)
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.sender_password = sender_password

    def execute(self, data_store: dict[str, Any]) -> dict[str, Any]:
        """Mock PDF extraction
        In real application, user can select recipient, subject, body, and attachments from the data_store (result of trigger + previous actions)
        """
        body = f"Thank you for your application. We have received the following information:\n\n{{user selected body from data_store}}"

        # Mock email sending
        print(f"Sending email to {{user selected recipient from data_store}}")
        print(f"Subject: {{user selected subject from data_store}}")
        print(f"Attachments: {{user selected attachments from data_store}}")
        print(f"Body: {body}")

        return {
            "status": "sent",
            "sender_email": self.sender_email,
            "recipient": f"{{user selected recipient from data_store}}",
        }
