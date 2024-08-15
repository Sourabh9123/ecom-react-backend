import json , requests



def get_token():
    try:
        account = 740561073
     
        url = "https://apis-sandbox.fedex.com/oauth/token"
        # url = "https://developer.fedex.com/api/en-us/catalog/authorization/v1/oauth/token"
        CLIENT_ID = "l766d06787d5e74caab05e4b54ef02941a"
        CLIENT_SECRATE = "893a7ac87968445e8b5ec6d6065c0b39"
        payload = {
            "grant_type" :"client_credentials",
            "client_id": CLIENT_ID,
            "client_secret" : CLIENT_SECRATE,
        }
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
            }

        response = requests.post(url, data=payload, headers=headers)

        # print(response.text)
        json_data = json.loads(response.text)
        return json_data
    except Exception as e:
        print(str(e))
        return "not authenticated"
