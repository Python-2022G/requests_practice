import requests
from pprint import pprint

URL = 'https://randommer.io/api/Name'
KEY = '2d794c6f46094ceb96bd719c1c26c984'

def get_name(name, n):
    payload = {
        'nameType': name,
        'quantity': n
    }
    header = {
        'X-Api-Key': KEY
    }

    response = requests.get(URL, params=payload, headers=header)
    return response.json()

name = 'fullname'
n = 5
names = get_name(name, n)

print(names)

