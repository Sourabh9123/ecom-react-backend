{

  "requestedShipment": {

    "shipper": {
      "address": {
        "streetLines": [
          "10 FedEx Parkway",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "CA",
        "postalCode": "90210",
        "countryCode": "US",
        "residential": False
      },
      "contact": {
        "personName": "John Taylor",
        "emailAddress": "sample@company.com",
        "phoneExtension": "91",
        "phoneNumber": "XXXX567890",
        "companyName": "Fedex"
      },
      
    },
    
    "recipients": [
      {
        "address": {
          "streetLines": [
            "10 FedEx Parkway",
            "Suite 302"
          ],
          "city": "Beverly Hills",
          "stateOrProvinceCode": "CA",
          "postalCode": "90210",
          "countryCode": "US",
          "residential": False
        },
        "contact": {
          "personName": "John Taylor",
          "emailAddress": "sample@company.com",
          "phoneExtension": "000",
          "phoneNumber": "XXXX345671",
          "companyName": "FedEx"
        },
       }
    ],

    "pickupType": "USE_SCHEDULED_PICKUP",
    "serviceType": "PRIORITY_OVERNIGHT",
    "packagingType": "YOUR_PACKAGING",

    "shippingChargesPayment": {
      "paymentType": "SENDER",
    },
    
   
   
    "labelSpecification": {
      "labelStockType": "PAPER_85X11_TOP_HALF_LABEL",
      "imageType": "PDF",
     
    },
   
   
   

    "requestedPackageLineItems": [
      {
        
        "weight": {
          "units": "KG",
          "value": 68
        },
      
      }
    ]
  },
  "labelResponseOptions": "LABEL",
  "accountNumber": {
    "value": "740561073"
  },
 
}






















###########################
{
  "requestedShipment": {
    "shipper": {
      "address": {
        "streetLines": [
          "10 FedEx Parkway",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "CA",
        "postalCode": "90210",
        "countryCode": "US",
        "residential": False
      },
      "contact": {
        "personName": "John Taylor",
        "emailAddress": "sample@company.com",
        "phoneExtension": "91",
        "phoneNumber": "XXXX567890",
        "companyName": "Fedex"
      }
    },
    "recipients": [
      {
        "address": {
          "streetLines": [
            "10 FedEx Parkway",
            "Suite 302"
          ],
          "city": "Beverly Hills",
          "stateOrProvinceCode": "CA",
          "postalCode": "90210",
          "countryCode": "US",
          "residential": False
        },
        "contact": {
          "personName": "John Taylor",
          "emailAddress": "sample@company.com",
          "phoneExtension": "000",
          "phoneNumber": "XXXX345671",
          "companyName": "FedEx"
        }
      }
    ],
    "pickupType": "USE_SCHEDULED_PICKUP",
    "serviceType": "PRIORITY_OVERNIGHT",
    "packagingType": "YOUR_PACKAGING",
    "shippingChargesPayment": {
      "paymentType": "SENDER",
      "payor": {
        "responsibleParty": {
          "accountNumber": "740561073",
          "contact": "",
          "address": {
            "countryCode": "US"
          }
        }
      }
    },
    "labelSpecification": {
      "labelStockType": "PAPER_85X11_TOP_HALF_LABEL",
      "imageType": "PDF"
    },
    "requestedPackageLineItems": [
      {
        "weight": {
          "units": "KG",
          "value": 68
        }
      }
    ]
  },
  "labelResponseOptions": "LABEL",
  "accountNumber": {
    "value": "740561073"
  }
}

