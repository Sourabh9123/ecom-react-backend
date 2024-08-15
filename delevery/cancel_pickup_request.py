import requests
import json
from delevery.fedex_authentication import pickup_authenticaton



def cancel_pick_up(fedex_confirmation_no): # cancel pickup ground
    token = pickup_authenticaton()
    print(token["access_token"])

    url = "https://apis-sandbox.fedex.com/pickup/v1/pickups/cancel"

    headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': "Bearer "+ str(token["access_token"])
        }
    
    
    payload = {
                "associatedAccountNumber": {
                    "value": "740561073"
                },
                "pickupConfirmationCode": "7",
                "remarks": "Please ring bell at loading dock.",
                "carrierCode": "FDXE",
                "accountAddressOfRecord": {
                    "streetLines": [
                    "123 Ship Street"
                    ],
                    "urbanizationCode": "URB FAIR OAKS",
                    "city": "Memphis",
                    "stateOrProvinceCode": "ON",
                    "postalCode": "38017",
                    "countryCode": "US",
                    "residential": False,
                    "addressClassification": "MIXED"
                },
                "scheduledDate": "2019-10-15",
                "location": "LOSA"
                }
    json_data = json.dumps(payload)

    response = requests.put(url, data=json_data, headers=headers)
    print(response.status_code)

    print(response.text)
    return response.status_code == 200 or False