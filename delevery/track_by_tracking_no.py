from delevery.fedex_authentication import get_token
import json
import requests

def tracking_details(tracking_number:int)-> dict:
    try:
        token = get_token()
        print(token.get("access_token"))
        url = "https://apis-sandbox.fedex.com/track/v1/trackingnumbers" # this is testing url not production

        payload = {
                "includeDetailedScans": True, 
                "trackingInfo": [
                    {
                    "shipDateBegin": "2020-03-29",
                    "shipDateEnd": "2020-04-01",
                    "trackingNumberInfo": {
                        "trackingNumber": str(tracking_number),
                        "carrierCode": "FDXE",
                        "trackingNumberUniqueId": "245822~123456789012~FDEG"
                    }
                    }
                    ]
                    }
        json_data = json.dumps(payload)


        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_us",
            'Authorization': "Bearer "+str(token.get("access_token")),
            }
        response = requests.post(url, data=json_data, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            pass
        
        json_data = json.loads(response.text)
        # print(json_data["output"]['completeTrackResults'])
        tracking_number_from_fedex =  json_data["output"]['completeTrackResults'][0]["trackingNumber"]
        # print(tracking_number_from_fedex)
        trackingNumberInfo = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["trackingNumberInfo"]
        # print(trackingNumberInfo)
        returnDetail = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["returnDetail"]
        # print(returnDetail)
        
        deliveryDetails = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["deliveryDetails"] # it contains details
        # print(deliveryDetails)
        scanEvents = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["scanEvents"]
        # print(scanEvents)
        recipientInformation = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["recipientInformation"]
        # print(recipientInformation)
        shipmentDetails =json_data["output"]['completeTrackResults'][0]["trackResults"][0]["shipmentDetails"]
        # print(shipmentDetails)
        shipperInformation = json_data["output"]['completeTrackResults'][0]["trackResults"][0]["shipperInformation"]
        # print(shipperInformation)
        
        return json_data
    except Exception as e:
        print(str(e))
        return "error occure"


