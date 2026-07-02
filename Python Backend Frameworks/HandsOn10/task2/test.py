import requests

url = "http://127.0.0.1:5002/api/students/1/enroll"

data = {
    "course_id": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.json())