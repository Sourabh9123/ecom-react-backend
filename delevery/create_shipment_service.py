from delevery.ship_api_authentication import get_token
from delevery.check_pickup_availability import pickup_authenticaton
import json, requests
#pickup and ship authentication are same added 
from delevery.cancel_shipment import cancel_shipment


def create_shipment_for_product():
    """
    it takes product and address of saller and customer
    for testing we are not taking anything for now

    """
    shipment_data = {
    'shipper_name': 'John Doe',
    'shipper_phone': '1234567890',
    'shipper_address': '123 Sender St',
    'shipper_city': 'Sender City',
    'shipper_state': 'CA',
    'shipper_postal_code': '90001',
    'shipper_country_code': 'US',
    'recipient_name': 'Jane Smith',
    'recipient_phone': '0987654321',
    'recipient_address': '456 Recipient St',
    'recipient_city': 'Recipient City',
    'recipient_state': 'NY',
    'recipient_postal_code': '10001',
    'recipient_country_code': 'US',
    'package_weight': 2.5,
    'package_length': 10,
    'package_width': 5,
    'package_height': 4
    }
    APIKEY = "l7e1b8908045844d7fb3dbf529dcd0dc11"
    secrate = "963487a5b76b4f3c8c22b6e66be8cd31"
    account = 740561073
    # "https://apis-sandbox.fedex.com/"
    
    url = "https://apis-sandbox.fedex.com/ship/v1/shipments"
    # https://developer.fedex.com/api/en-us/catalog/ship/v1/ship/v1
    # url = "https://wsbeta.fedex.com:443/web-services/api/en-us/catalog/ship/v1/ship/v1/shipments"
    # https://wsbeta.fedex.com

    token = get_token()
    # token = pickup_authenticaton()
    print(token)
    print("-------------------------------------------------------------")
    # print(pickup_authenticaton())
    headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': "Bearer " + str(token["access_token"]),

        }
    

    payload = {
  "labelResponseOptions": "URL_ONLY",
  "requestedShipment": {
    "shipper": {
      "contact": {
        "personName": "sourabh kumar das",
        "phoneNumber": 1234567890,
        "companyName": "Shipper Company Name"
      },
      "address": {
        "streetLines": [
          ""
        ],
        "city": "Mumbai",
        "stateOrProvinceCode": "MH",
        "postalCode": 400001,
        "countryCode": "IN"
      }
    },
    "recipients": [
      {
        "contact": {
          "personName": "sumit das",
          "phoneNumber": 1234567890,
          "companyName": "Recipient Company Name"
        },
        "address": {
          "streetLines": [
            "rama nath paul road "
          ],
          "city": "Kolkata",
          "stateOrProvinceCode": "WB",
          "postalCode": 700023,
          "countryCode": "IN",
          "residential": True
        }
      }
    ],
    "shipDatestamp": "2024-05-31",#yyyy-mm-dd
    "serviceType": "GROUND_HOME_DELIVERY",
    "packagingType": "YOUR_PACKAGING",
    "pickupType": "USE_SCHEDULED_PICKUP",
    "blockInsightVisibility": False,
    "shippingChargesPayment": {
      "paymentType": "SENDER"
    },
    "shipmentSpecialServices": {
      "specialServiceTypes": [
        "HOME_DELIVERY_PREMIUM"
      ],
      "homeDeliveryPremiumDetail": {
        "homedeliveryPremiumType": "APPOINTMENT",
        "deliveryDate": "2024-05-01",
        "phoneNumber": {
          "localNumber": 1234567890
        }
      }
    },
    "labelSpecification": {
      "imageType": "PDF",
      "labelStockType": "PAPER_85X11_TOP_HALF_LABEL"
    },
    "requestedPackageLineItems": [
      {
        "weight": {
          "units": "KG",
          "value": 1
        }
      }
    ]
  },
  "accountNumber": {
    "value": "740561073"
  }
}

    
    jsno_data = json.dumps(payload)

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response = response.json()
    else:
        return "Error occured"
   
   
    transaction_id = response['transactionId']
    master_tracking_number = response['output']['transactionShipments'][0]['masterTrackingNumber']
    service_type = response['output']['transactionShipments'][0]['serviceType']
    service_name = response['output']['transactionShipments'][0]['serviceName']
    ship_date = response['output']['transactionShipments'][0]['shipDatestamp']
    delivery_date = response['output']['transactionShipments'][0]['pieceResponses'][0]['deliveryDatestamp']
    tracking_number = response['output']['transactionShipments'][0]['pieceResponses'][0]['trackingNumber']
    package_document_url = response['output']['transactionShipments'][0]['pieceResponses'][0]['packageDocuments'][0]['url']
    base_rate_amount = response['output']['transactionShipments'][0]['pieceResponses'][0]['baseRateAmount']
    # total_net_charge = response['output']['transactionShipments'][0]['shipmentRating']['shipmentRateDetails'][0]['totalNetCharge']
    # surcharges = response['output']['transactionShipments'][0]['shipmentRating']['shipmentRateDetails'][0]['surcharges']
    print(transaction_id)
    print(master_tracking_number)
    print(service_type)
    print(service_name)
    print(ship_date)
    print(delivery_date)
    print(tracking_number)
    print(package_document_url)
    print(base_rate_amount*82)


    # print(total_net_charge)
    # print(surcharges)
   
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     response.raise_for_status()




"""

 {
        "requestedShipment" : {
            "shipper" : {
                "address": {
                            "streetLines" : [],
                            "city" : "lesst than 35 char",
                            "countryCode" : "IN"
                            },
                
                "contact" : {
                    "personName" : "",
                    "emailAddress" : "",
                    "phoneNumber" : "reqired"
                }

            }
            ,
            "recipients" : [
                {
                 "address":{
                     "streetLines": [],
                     "city": "",
                     "countryCode": "IN",
                     
                 },
                 "contact" : {
                     "phoneNumber": "required",
                     "personName": "John Taylor",
                     "emailAddress": "sample@company.com",
                 }   
                }
            ]
          },
      "pickupType":"USE_SCHEDULED_PICKUP"# need to see that
      ,
      "serviceType": "FEDEX_GROUND",
      "packagingType" : "YOUR_PACKAGING",
      "shippingChargesPayment":{
          "paymentType": "RECIPIENT",

      },
      "labelSpecification":{
          "labelStockType": "PAPER_4X8",
          "imageType": "PNG",
          
      },
      "requestedPackageLineItems": [
          {
              "weight":{
                  "units" : "KG",
                  "value": "0.250"
              }
          }
      ],
    "labelResponseOptions": "URL_ONLY",
    "accountNumbe" : {
        "value" : "740561073"
    }
    }


"""





















{
  "labelResponseOptions": "URL_ONLY",
  "requestedShipment": {
    "shipper": {
      "contact": {
        "personName": "SHIPPER NAME",
        "phoneNumber": 9018328595
      },
      "address": {
        "streetLines": [
          "SHIPPER STREET LINE 1",
          "SHIPPER STREET LINE 2"
        ],
        "city": "Pune",
        "stateOrProvinceCode": "MH",
        "postalCode": 411039,
        "countryCode": "IN"
      }
    },
    "recipients": [
      {
        "contact": {
          "personName": "RECIPIENT NAME",
          "phoneNumber": 9018328595
        },
        "address": {
          "streetLines": [
            "RECIPIENT STREET LINE 1",
            "RECIPIENT STREET LINE 2"
          ],
          "city": "Chennai",
          "stateOrProvinceCode": "TN",
          "postalCode": 600066,
          "countryCode": "IN"
        }
      }
    ],
    "shipDatestamp": "2020-07-03",
    "serviceType": "STANDARD_OVERNIGHT",
    "packagingType": "YOUR_PACKAGING",
    "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
    "blockInsightVisibility": False,
    "shippingChargesPayment": {
      "paymentType": "SENDER"
    },
    "shipmentSpecialServices": {
      "specialServiceTypes": [
        "DELIVERY_ON_INVOICE_ACCEPTANCE",
        "COD"
      ],
      "shipmentCODDetail": {
        "codCollectionAmount": {
          "amount": 2000,
          "currency": "INR"
        },
        "codCollectionType": "CASH",
        "codRecipient": {
          "contact": {
            "personName": "DIA NAME",
            "phoneNumber": 1234567890
          },
          "address": {
            "streetLines": [
              "301 E MAIN ST"
            ],
            "city": "Chennai",
            "stateOrProvinceCode": "TN",
            "postalCode": 600066,
            "countryCode": "IN"
          }
        }
      },
      "deliveryOnInvoiceAcceptanceDetail": {
        "recipient": {
          "contact": {
            "personName": "DIA Name",
            "phoneNumber": 1234567890
          },
          "address": {
            "streetLines": [
              "Street line 1",
              "Street line 2"
            ],
            "city": "PUNE",
            "stateOrProvinceCode": "MH",
            "postalCode": 411039,
            "countryCode": "IN"
          }
        }
      }
    },
    "labelSpecification": {
      "imageType": "PDF",
      "labelStockType": "PAPER_85X11_TOP_HALF_LABEL"
    },
    "customsClearanceDetail": {
      "isDocumentOnly": False,
      "dutiesPayment": {
        "paymentType": "SENDER"
      },
      "commercialInvoice": {
        "shipmentPurpose": "SOLD"
      },
      "freightOnValue": "CARRIER_RISK",
      "commodities": [
        {
          "description": "DSLR Camera",
          "countryOfManufacture": "US",
          "weight": {
            "value": 20,
            "units": "KG"
          },
          "quantity": 1,
          "quantityUnits": "PCS",
          "unitPrice": {
            "amount": 2000,
            "currency": "INR"
          },
          "customsValue": {
            "amount": 2000,
            "currency": "INR"
          }
        }
      ]
    },
    "requestedPackageLineItems": [
      {
        "weight": {
          "units": "KG",
          "value": 20
        }
      }
    ]
  },
  "accountNumber": {
    "value": "XXX561073"
  }
}