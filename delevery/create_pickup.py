from delevery.fedex_authentication import pickup_authenticaton
import requests
import json

def create_pickup(address, user):
    url = "https://apis-sandbox.fedex.com/pickup/v1/pickups"

    token = pickup_authenticaton()
    print(token["access_token"])
    headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': "Bearer " + str(token["access_token"]),
        }

    payload = {
    "associatedAccountNumber": {"value": "740561073"},
    "originDetail": {
        "pickupLocation": {
            "contact": {"companyName": "Atos Syntel", "personName": "Suresh", "phoneNumber": "8444869123"},
            "address": {
                "streetLines": ["5/3 rama nath paul road khidderpore ",],
                "city": "kolkata",
                "stateOrProvinceCode": "WB",
                "postalCode": "700023",
                "countryCode": "IN",
                "residential": True
            }
        },
        "readyDateTimestamp": "2024-05-22T11:00:00Z",
        "customerCloseTime": "2024-05-24T11:00:00Z"
    },
    "carrierCode": "FDXE"
}

    json_data = json.dumps(payload)
    response = requests.post(url, data=json_data, headers=headers)
    print(response.text)
    print(response.status_code)

    return "success"




