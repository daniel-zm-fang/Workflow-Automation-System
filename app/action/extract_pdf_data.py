from .base import BaseAction
from typing import Any
import json
from app.constant.constants import JSON_SCHEMA_TEMPLATES


class ExtractPDFDataAction(BaseAction):
    def __init__(self, name: str, template_id: str):
        super().__init__(name)
        self.template_id = template_id
        self.schema_path = JSON_SCHEMA_TEMPLATES[template_id]
        with open(self.schema_path, "r") as schema_file:
            self.schema = json.load(schema_file)

    def execute(self, data_store: dict[str, Any]) -> dict[str, Any]:
        """Mock PDF extraction
        In real application, user can select which PDFs to extract from the data_store (result of trigger + previous actions)
        """
        extracted_data = None

        if self.template_id == "company_a":
            extracted_data = {
                "full_name": "John Doe",
                "date_of_birth": "1990-01-01",
                "address": "123 Main St, Anytown, USA",
                "phone_number": "+1234567890",
                "email": "johndoe@example.com",
            }
        elif self.template_id == "company_b":
            extracted_data = {
                "personalInfo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "dateOfBirth": "1990-01-01",
                    "phoneNumber": "+1234567890",
                    "email": "johndoe@example.com",
                },
                "insuranceInfo": {
                    "policyNumber": "ABC123",
                    "policyType": "life",
                },
            }
        else:
            raise ValueError(f"Invalid template ID: {self.template_id}")
        return {"extracted_data": extracted_data}
