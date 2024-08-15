import requests
import json


def get_shiprocket_token():
    url = "https://apiv2.shiprocket.in/v1/external/auth/login"

    payload = json.dumps({
    "email": "gyroboy02@gmail.com",
    "password": "9038677525Soura"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        # print(response.text)
        return response.json()
    else:
        return "authentication failed"


def get_all_the_pickup_address():
    token = get_shiprocket_token()
    print(token)

    url = "https://apiv2.shiprocket.in/v1/external/settings/company/pickup"

    payload={}
    headers = {
    'Authorization': f'Bearer {token["token"]}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
