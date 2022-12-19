import requests

URL = 'https://randomuser.me/api/'
payload = {
    'results': 10,
    'gender': 'male'
}

response = requests.get(URL, params=payload)

print(response.url)