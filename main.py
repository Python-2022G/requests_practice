import requests

URL = 'https://randomuser.me/api/'
payload = {
    'results': 3,
    'gender': 'male',
    'nat': 'US'
}

response = requests.get(URL, params=payload)

print(response.url)
print(response.json())