import requests

url = "http://127.0.0.1:5000/api/enroll/1"

data = {
    "course_id": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.json())