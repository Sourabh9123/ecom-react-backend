import requests
import json
from shiprocket.authentication import get_shiprocket_token
from datetime import datetime

"""
for more deatils look into to the documentation

link:https://apidocs.shiprocket.in/#4ba045ab-e25b-4bb1-adbd-37bbd07b354e

"""


def create_quick_order(address, product_id):
    date_time_now = datetime.now()
    print("-----------------------------",date_time_now)



    url = "https://apiv2.shiprocket.in/v1/external/orders/create/adhoc"
    token = get_shiprocket_token()

    payload = json.dumps({
   
    "order_id": "224-447",
    "order_date": "2024-01-24 11:11",
    "pickup_location": "Primary",
    "channel_id": "",
    "comment": "Reseller: M/s Goku",
    "billing_customer_name": "Naruto",
    "billing_last_name": "Uzumaki",
    "billing_address": "House 221B, Leaf Village",
    "billing_address_2": "Near Hokage House",
    "billing_city": "New Delhi",
    "billing_pincode": "110002",
    "billing_state": "Delhi",
    "billing_country": "India",
    "billing_email": "naruto@uzumaki.com",
    "billing_phone": "9876543210",
    "shipping_is_billing": True,
    "shipping_customer_name": "",
    "shipping_last_name": "",
    "shipping_address": "",
    "shipping_address_2": "",
    "shipping_city": "",
    "shipping_pincode": "",
    "shipping_country": "",
    "shipping_state": "",
    "shipping_email": "",
    "shipping_phone": "",
    "order_items": [
        {
        "name": "Kunai",
        "sku": "chakra123",
        "units": 10,
        "selling_price": "900",
        "discount": "",
        "tax": "",
        "hsn": 441122
        }
    ],
    "payment_method": "Prepaid",
    "shipping_charges": 0,
    "giftwrap_charges": 0,
    "transaction_charges": 0,
    "total_discount": 0,
    "sub_total": 9000,
    "length": 10,
    "breadth": 15,
    "height": 20,
    "weight": 2.5
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token["token"]}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
