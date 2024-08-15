from delevery.fedex_authentication import pickup_authenticaton
import requests
import json



def check_pickup_availability(address:object, user:object)-> bool:
    token = pickup_authenticaton()
    print(token["access_token"])

    
    url = "https://apis-sandbox.fedex.com/pickup/v1/pickups/availabilities"

    
    headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': "Bearer " + str(token["access_token"])
        }
    

    payload = {
                "pickupAddress": {
                    "postalCode": "700023",
                    "countryCode": "IN"
                },
                "pickupRequestType": [
                    "FUTURE_DAY"
                ],
                "carriers": [
                    "FDXG"
                ],
                "countryRelationship": "DOMESTIC"
            }
    json_data = json.dumps(payload)

    response = requests.post(url, data=json_data, headers=headers)

    print(response.text)
    return  response.status_code == 200 or False
