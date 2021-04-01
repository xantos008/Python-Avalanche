import requests
import json

url = 'https://useavalanche.us.auth0.com/oauth/token'
body = {
    'client_id': 'ertuRwxTMB6k8cV5LIZVg5nWTosIyVUH',
    'client_secret': 'Ls2aqX4pEp8npwx3yk6OeZq8ETbtdWPYqOcnepaKIHIr1u0U5b4XoDXsJaKyufeP',
    'audience': 'https://useavalanche.us.auth0.com/api/v2/',
    'grant_type': 'client_credentials'}
# headers for json response
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(body), headers=headers)
data = r.json()

token = data['token_type'] + " " + data['access_token']

url = 'http://salty-reef-38656.herokuapp.com//events/premium_event'
body = {
    'email': 'your@user.email'
}
# headers for json response
headers = {'Content-type': 'application/json', 'authorization': token}

r = requests.post(url, data=json.dumps(body), headers=headers)
