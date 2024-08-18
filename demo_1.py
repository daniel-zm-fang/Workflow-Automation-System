import requests
import json

base_url = "http://localhost:5001/api"

# Run a one-off workflow
print("Running one-off workflow:")
one_off_url = f"{base_url}/run_one_off_pdf_email_workflow"
payload = {
    "imap_server": "imap.example.com",
    "smtp_server": "smtp.example.com",
    "email_address": "your_email@example.com",
    "email_password": "your_password",
    "company": "company_a",
}
headers = {"Content-Type": "application/json"}

response = requests.post(one_off_url, data=json.dumps(payload), headers=headers)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=4)}")

# Start a persistent workflow
print("\nStarting persistent workflow:")
persistent_url = f"{base_url}/start_persistent_pdf_email_workflow"
response = requests.post(persistent_url, data=json.dumps(payload), headers=headers)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=4)}")
