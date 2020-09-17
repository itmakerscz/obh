import requests
import json

headers = {'content-type': 'application/json'}
url = 'https://api.finqware.com/v1/sessions'

data = {
  'nonce': '',
  'session_id': '',
  'status': ''
  }

params = {
    'client_id':'577fc3d1-c713-4551-aee5-3ce8e0ec8f8e',
    'client_app_key':'MDAxNmxvY2F0aW9uIGZpbnF3YXJlCjAwMWNpZGVudGlmaWVyIGl0bWFrZXJzLWRldgowMDE2Y2lkIHNjb3BlPXNlc3Npb24KMDAzN2NpZCBjbGllbnRfaWQ9NTc3ZmMzZDEtYzcxMy00NTUxLWFlZTUtM2NlOGUwZWM4ZjhlCjAwMmZzaWduYXR1cmUg0GjaeETZGNwcLH6d9zXDeoQ3COo-sQoBTU44CUcUT-AK',
    'skill':'erste_hr_aisp_sbx_#1.0'
    }

r = requests.post(url, params=params, headers=headers)

print(r)
print(r.json())
