import requests
import json

url = "http://localhost:5001/api/run_scheduled_dummy_action_every_ten_second"
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers)

print(f"Status code: {response.status_code}")
print(f"Request Headers: {response.headers}")
print(f"Response: {json.dumps(response.json(), indent=4)}")
