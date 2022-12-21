import requests
import json
url = "https://randommer.io/api/Card"
payload = {
    "type": "visa"
}
header = {
    "X-Api-Key": "f430c121f8694734bd0b530c6a059ef2"
}

response = requests.get(url = url, params= payload , headers=header)
data = json.dumps(response, indent=4)
with open("data01.json", mode="w") as file:
    file.write(data)