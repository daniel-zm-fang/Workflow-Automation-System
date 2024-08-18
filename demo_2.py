import requests
import json

base_url = "http://localhost:5001/api"

# Start a persistent scheduled dummy workflow
print("Starting persistent scheduled dummy workflow:")
url = f"{base_url}/start_persistent_scheduled_dummy_workflow"
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=4)}")

# List all workflows
print("\nListing all workflows:")
list_url = f"{base_url}/list_workflows"
response = requests.get(list_url)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=4)}")

# To stop a workflow, uncomment and use:
# workflow_id = "replace_me_with_workflow_id"
# stop_url = f"{base_url}/stop_workflow/{workflow_id}"
# response = requests.post(stop_url)
# print(f"\nStopping workflow {workflow_id}:")
# print(f"Status code: {response.status_code}")
# print(f"Response: {json.dumps(response.json(), indent=4)}")
