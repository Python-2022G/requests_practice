import requests
from pprint import pprint

URL = 'https://randommer.io/api/Card'
payload = {
    'type': 'Mastercard'
}
header = {
    'X-Api-Key': '2d794c6f46094ceb96bd719c1c26c984'
}

response = requests.get(URL, params=payload, headers=header)

print(response.url)
pprint(response.json())