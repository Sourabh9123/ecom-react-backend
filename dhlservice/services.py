import requests
from django.conf import settings

class DHLService:
    def __init__(self):
        self.base_url = "https://express.api.dhl.com/mydhlapi/test"
        self.api_key = "wyXgKncvkFxHJz96eylGwW0Ld4MaJy7Q.DHL_API_KEY"
        self.secret_key = "2tkizjvOWPv5AnFz"

    def create_shipment(self, shipment_details):
        url = f"{self.base_url}/shipments"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}:{self.secret_key}'
        }
        response = requests.post(url, json=shipment_details, headers=headers)
        return response.json()

    def track_shipment(self, tracking_number):
        url = f"{self.base_url}/track/shipments/{tracking_number}"
        headers = {
            'Authorization': f'Bearer {self.api_key}:{self.secret_key}'
        }
        response = requests.get(url, headers=headers)
        return response.json()



























# {
#     "consignee": {
#         "name": "John Doe",
#         "address": "123 Main St",
#         "city": "Berlin",
#         "countryCode": "DE",
#         "postalCode": "10115"
#     },
#     "shipper": {
#         "name": "Jane Smith",
#         "address": "456 Elm St",
#         "city": "Munich",
#         "countryCode": "DE",
#         "postalCode": "80331"
#     },
#     "packages": [
#         {
#             "weight": 1.5,
#             "length": 10,
#             "width": 5,
#             "height": 8
#         }
#     ]
# }
