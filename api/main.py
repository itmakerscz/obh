import requests
import json

# client id from https://developers.finqware.com
client_id =  '577fc3d1-c713-4551-aee5-3ce8e0ec8f8e'
# client app key from https://developers.finqware.com
client_app_key = 'MDAxNmxvY2F0aW9uIGZpbnF3YXJlCjAwMWNpZGVudGlmaWVyIGl0bWFrZXJzLWRldgowMDE2Y2lkIHNjb3BlPXNlc3Npb24KMDAzN2NpZCBjbGllbnRfaWQ9NTc3ZmMzZDEtYzcxMy00NTUxLWFlZTUtM2NlOGUwZWM4ZjhlCjAwMmZzaWduYXR1cmUg0GjaeETZGNwcLH6d9zXDeoQ3COo-sQoBTU44CUcUT-AK'
# skill from https://developers.finqware.com and your chosen sandbox
skill = 'erste_hr_aisp_sbx_#1.0'

# send headers for post request
headers = {'content-type': 'application/json'}
# send url for post request
url_base = 'https://api.finqware.com/v1/sessions'

# send params for post request
params = {
    'client_id': client_id,
    'client_app_key': client_app_key,
    'skill': skill
    }

url = url_base

req_get = requests.post(url, json = params, headers = headers)
# print(req_get.status_code)
if req_get.status_code != 200:
    print('POST /v1/sessions/ {}' + req_get.status_code)
# print(req_get.json()['nonce'])
# req_get = requests.post(url, params = params, headers = headers)

# recieved data from send for post request
req_json = {
    'nonce': '',
    'session_id': '',
    'status': ''
}

req_json = req_get.json()

#print(req_get.text)
print(req_json['nonce'])


# send params for post request
params = {
    'client_id': client_id,
    'nonce': req_json['nonce'],
    'skill': skill,
    'step': 'sca',
    'data': {
        'psu_redirect_link': 'itmakers://itmakers.cz'
    }
}
# send url for post request
url = url_base + '/' + req_json['session_id'] + '/steps'

req_get = requests.post(url, json = params, headers = headers)
# print(req_get.status_code)
if req_get.status_code != 200:
    print('POST /v1/sessions/:id/steps {}' + req_get.status_code)
# get send post data
# req_get = requests.post(url, params = params, headers = headers)

# recieved data from send for post request
req_json = {
    'data': {
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded'
            },
        'method': 'GET',
        'url': 'itmakers.cz'
        },
    'status': 'SESSION_IN_PROGRESS'
}

req_json = req_get.json()

print('\n')
print(req_get.text)
#print(req_json.nonce)
