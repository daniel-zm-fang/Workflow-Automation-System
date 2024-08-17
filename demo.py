import requests
import json

url = "http://localhost:5001/api/run_workflow"
payload = {
    "imap_server": "imap.example.com",
    "smtp_server": "smtp.example.com",
    "email_address": "your_email@example.com",
    "email_password": "your_password",
    "company": "company_a",
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(f"Status code: {response.status_code}")
print(f"Request Headers: {response.headers}")
print(f"Response: {json.dumps(response.json(), indent=4)}")
