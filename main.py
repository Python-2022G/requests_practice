import requests
import json
i = 0
data_user = []
while i <=100:
    response = requests.get("https://random.dog/woof.json")
    if response.status_code == 200:
        data = response.json()
        data_user.append(data)
    i += 1
data_dog = json.dumps(data_user, indent=4)

with open("users.json", mode="w") as file:
    file.write(data_dog)