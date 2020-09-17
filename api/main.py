import requests

r = requests.get('https://api.firmquare.com')
print(r)
print(r.content)
