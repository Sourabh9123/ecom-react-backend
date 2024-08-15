

import requests
import json


def get_token():
    try:
        token = ""
        url = "https://apis-sandbox.fedex.com/oauth/token"
        CLIENT_ID = "l7ca3ae01f605e4b8a93e01294f236c067"
        CLIENT_SECRATE = "9438a44b4bab4b1ba4ca5f4010eb46bc"
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



def pickup_authenticaton():
    
    try:
        token = ""
        url = "https://apis-sandbox.fedex.com/oauth/token"
        # url = "https://developer.fedex.com/api/en-us/catalog/authorization/v1/oauth/token"
        CLIENT_ID = "l7e1b8908045844d7fb3dbf529dcd0dc11"
        CLIENT_SECRATE = "963487a5b76b4f3c8c22b6e66be8cd31"
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
