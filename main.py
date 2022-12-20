import requests
from pprint import pprint

url = 'https://random.dog/woof.json'
s = ''


for i in range(100):
    r = requests.get(url)
    r = r.json()
    link = r['url']
    s+=link+ '\n'
    
with open("file.txt", "w") as text_file:
    # print(s)
    text_file.write(s)