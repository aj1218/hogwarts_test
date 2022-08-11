import requests
import json

url = r"https://gw.ininin.com/byt-user/user/login_new"
payload = json.dumps({
    "userName": "0003",
    "password": "123456"
})
headers = {
    'applicationId': '1621914135658',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload).json()
session = response["data"]["access_token"]
Authorization = 'bearer {}'.format(session)
print(Authorization)
url = "https://gw.ininin.com/byt-user/user/current/user"

payload={}
headers = {
  'access_token': session,
  'applicationId': '1621914135658',
  'Authorization': Authorization
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
