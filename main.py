import requests
from pprint import pprint

URL = 'https://randomuser.me/api/'
payload = {
    'results': 3,
    'gender': 'male',
    'nat': ['US', 'BR'],
    'inc': 'name'
}

response = requests.get(URL, params=payload)

print(response.url)
pprint(response.json())