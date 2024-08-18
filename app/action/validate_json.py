from .base import BaseAction
from typing import Any
import json
import jsonschema
from app.constant.constants import JSON_SCHEMA_TEMPLATES


class ValidateDataAction(BaseAction):
    def __init__(self, name: str, template_id: str):
        super().__init__(name)
        self.template_id = template_id
        self.schema_path = JSON_SCHEMA_TEMPLATES[template_id]
        with open(self.schema_path, "r") as schema_file:
            self.schema = json.load(schema_file)

    def execute(self, data_store: dict[str, Any]) -> dict[str, Any]:
        # Look for the extracted_data in the previous action's result
        extracted_data = data_store.get("Extract PDF Data", {}).get("extracted_data")
        if not extracted_data:
            raise ValueError("No extracted data found in data store")

        try:
            jsonschema.validate(instance=extracted_data, schema=self.schema)
            return {"validation_result": "success"}
        except jsonschema.exceptions.ValidationError as e:
            return {"validation_result": "failure", "error_message": e.__repr__()}
