from delevery.ship_api_authentication import get_token
import requests, json



def cancel_shipment(tracking_number):# it take tracking number then cancel it
    
    # url = "https://developer.fedex.com/api/en-us/catalog/ship/v1/ship/v1/shipments/cancel"
    
    url = "https://apis-sandbox.fedex.com/ship/v1/shipments/cancel"
    token = get_token()
    headers = {
    'Content-Type': "application/json",
    'X-locale': "en_US",
    'Authorization': "Bearer "+ str(token["access_token"])
    }

    payload = {
  "accountNumber": {
    "value": "740561073"
  },
  "trackingNumber": tracking_number
}

    response = requests.put( url, headers=headers,  json=payload )
    print(response.status_code)
    # print(response.json())
    return response.json()

