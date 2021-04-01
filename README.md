# ****Python Avalanche| Get Token | Sample Code****

`pip install requests`

****OR****

If you work with Python packages, use virtual environment

`pipenv install requests`

File with comments

    # import library for HttpRequests
    import requests
    # import library for work with json (basically you can do in online string)
    import json
    
    # url for request
    url = 'https://useavalanche.us.auth0.com/oauth/token'
    # client_id and client_secret you can get in your dashboard
    # Go to https://refer-customer-dashboard.vercel.app/ if you don't know it yet
    # audience and grant_type stays the same, never change it!
    # Also we past your real client_id and client_secret from your account in our system with email samyang@letsthryft.com
    body = {
        'client_id': 'ertuRwxTMB6k8cV5LIZVg5nWTosIyVUH',
        'client_secret': 'Ls2aqX4pEp8npwx3yk6OeZq8ETbtdWPYqOcnepaKIHIr1u0U5b4XoDXsJaKyufeP',
        'audience': 'https://useavalanche.us.auth0.com/api/v2/',
        'grant_type': 'client_credentials'}
    # headers for json response
    headers = {'content-type': 'application/json'}
    
    # r - variable which contains all response data
    r = requests.post(url, data=json.dumps(body), headers=headers)
    # data - variable which contains json answer, if .json() is wrong, there would be an Exception
    data = r.json()
    
    # Make your token from its type and encodings
    token = data['token_type'] + " " + data['access_token']
    
    # print(token) will show you
    # Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCI...
    
    # Happy coding! :-)
    
