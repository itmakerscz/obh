import requests

r = requests.get('https://api.firquare.com')
print(r)
print(r.content)
