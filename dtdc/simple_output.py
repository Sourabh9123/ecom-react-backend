import requests






def dtdc():
        

    url = "https://www.clickpost.in/api/v3/create-order/"
    url = "https://www.clickpost.in/api/v3/create-order/?username=test-enterprise&key=92we9be53de84223ad14d7391159b80e"

    payload = {
        "drop_info": {
            "drop_lat": 0,
            "drop_city": "Mumbai",
            "drop_long": 0,
            "drop_name": "dsadsad sadsad",
            "drop_email": "something@something.com",
            "drop_phone": "9876543210",
            "drop_state": "Maharashtra",
            "drop_address": "123 ABC St",
            "drop_district": "Mumbai City",
            "drop_landmark": None,
            "drop_pincode": "400065",
            "drop_country": "IN",
            "drop_address_type": "OFFICE"
        },
        "pickup_info": {
            "pickup_lat": 25.1414664,
            "pickup_city": "Mumbai",
            "pickup_long": 55.255369,
            "pickup_name": "TEST DO NOT PICKUP",
            "pickup_time": "2022-10-271T11:52:36+04:00",
            "pickup_email": "abcd@defg.com",
            "pickup_phone": "1234567890",
            "pickup_state": "Maharashtra",
            "pickup_address": "123, ABC St",
            "pickup_district": "Mumbai City",
            "pickup_landmark": None,
            "pickup_phone_code": "+971",
            "pickup_pincode": "400065",
            "pickup_country": "IN",
            "pickup_address_type": "RESIDENTIAL"
        },
        "shipment_details": {
            "items": [
                {
                    "sku": "53813",
                    "price": 249.29,
                    "weight": 500,
                    "hs_code": "6405.10.00",
                    "quantity": 1,
                    "description": "Tod's Blue Patent Cutout Ankle Strap Ballet Flats Size 39.5",
                    "manufacture_country": "Italy",
                    "manufacture_country_code": "IT",
                    "cat": "Footwear",
                    "color": "Blue",
                    "brand": "Allen Solly",
                    "size": "Small"
                }
            ],
            "height": 13,
            "length": 23,
            "weight": 1000,
            "breadth": 31,
            "order_id": "TESTORDER0001",
            "cod_value": 50,
            "order_type": "COD",
            "invoice_date": "2022-06-21",
            "delivery_type": "RVP",
            "rvp_reason": "Defective product",
            "invoice_value": 468.58,
            "invoice_number": "TLC-2022-06-WS-00038",
            "courier_partner": "129",
            "reference_number": "TESTORDER000001",
            "account_code": "test"
        },
        "additional": {
            "return_info": {
                "lat": 25.1414664,
                "city": "Mumbai",
                "long": 55.255369,
                "name": "TEST DO NOT RETURN",
                "email": "abcd@defg.com",
                "phone": "1234567890",
                "state": "Maharashtra",
                "address": "123, ABC St",
                "district": "Mumbai City",
                "landmark": None,
                "pincode": "400065",
                "country": "IN"
            },
            "async": False,
            "label": True
        },
        "gst_info": {
            "seller_gstin": "1234",
            "taxable_value": 100,
            "ewaybill_serial_number": "2345677",
            "is_seller_registered_under_gst": False,
            "sgst_tax_rate": 100,
            "place_of_supply": "DELHI",
            "gst_discount": 0,
            "hsn_code": "1234",
            "sgst_amount": 100,
            "enterprise_gstin": "13",
            "gst_total_tax": 100,
            "igst_amount": 100,
            "cgst_amount": 200,
            "gst_tax_base": 200,
            "consignee_gstin": "1233",
            "igst_tax_rate": 100,
            "invoice_reference": "1234",
            "cgst_tax_rate": 100
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)



# def dtdc():
#     pass
#     url = "https://www.clickpost.in/api/v3/create-order/"
#     headers = {
#     "accept": "application/json",
#     "content-type": "application/json"
#     }
    
#     payload = {
# 	"drop_info": {
# 		"drop_lat": 0,
# 		"drop_city": "Mumbai",
# 		"drop_long": 0,
# 		"drop_name": "dsadsad sadsad",
# 		"drop_email": "something@something.com",
# 		"drop_phone": "9876543210",
# 		"drop_state": "Maharashtra",
# 		"drop_address": "123 ABC St",
# 		"drop_district": "Mumbai City",
# 		"drop_landmark": "",
# 		"drop_pincode": "400065",
# 		"drop_country": "IN",
# 		"drop_address_type": "RESIDENTIAL"
# 	},
# 	"pickup_info": {
# 		"pickup_lat": 25.1414664,
# 		"pickup_city": "Mumbai",
# 		"pickup_long": 55.255369,
# 		"pickup_name": "TEST DO NOT PICKUP",
# 		"pickup_time": "2022-10-271T11:52:36+04:00",
# 		"pickup_email": "abcd@defg.com",
# 		"pickup_phone": "1234567890",
# 		"pickup_state": "Maharashtra",
# 		"pickup_address": "123, ABC St",
# 		"pickup_district": "Mumbai City",
# 		"pickup_landmark": "",
# 		"pickup_phone_code": "+971",
# 		"pickup_pincode": "400065",
# 		"pickup_country": "IN",
# 		"pickup_address_type": "OFFICE"
# 	},
# 	"shipment_details": {
# 		"items": [{
# 			"sku": "53813",
# 			"price": 249.29,
# 			"weight": 500,
# 			"hs_code": "6405.10.00",
# 			"quantity": 1,
# 			"description": "Tod's Blue Patent Cutout Ankle Strap Ballet Flats Size 39.5",
# 			"manufacture_country": "Italy",
# 			"manufacture_country_code": "IT",
# 			"cat": "Footwear",
# 			"color": "Blue",
# 			"brand": "Allen Solly",
# 			"size": "Small",
# 			"final_amount_paid": "200.29",
# 			"store_credits_used": "49.00"
# 		}],
# 		"height": 13,
# 		"length": 23,
# 		"weight": 1000,
# 		"breadth": 31,
# 		"order_id": "TESTORDER0001",
# 		"cod_value": 50,
# 		"order_type": "COD",
# 		"invoice_date": "2022-06-21",
# 		"delivery_type": "FORWARD",
# 		"invoice_value": 468.58,
# 		"invoice_number": "TLC-2022-06-WS-00038",
# 		"courier_partner": "129",
# 		"reference_number": "TESTORDER000001",
# 		"account_code": "test"
# 	},
# 	"additional": {
# 		"return_info": {
# 			"lat": 25.1414664,
# 			"city": "Mumbai",
# 			"long": 55.255369,
# 			"name": "TEST DO NOT RETURN",
# 			"email": "abcd@defg.com",
# 			"phone": "1234567890",
# 			"state": "Maharashtra",
# 			"address": "123, ABC St",
# 			"district": "Mumbai City",
# 			"landmark": "",
# 			"pincode": "400065",
# 			"country": "IN"
# 		},
# 		"estimated_delivery_date": "2023-12-05",
# 		"async": False,
# 		"label":True,
# 		"user_defined_field_array": [{
# 				"name": "udf_1",
# 				"type": "String",
# 				"value": ""
# 			},
# 			{
# 				"name": "udf_2",
# 				"type": "String",
# 				"value": ""
# 			},
# 			{
# 				"name": "udf_3",
# 				"type": "String",
# 				"value": ""
# 			},
# 			{
# 				"name": "udf_4",
# 				"type": "String",
# 				"value": ""
# 			}
# 		]
# 	},
# 	"gst_info": {
# 		"seller_gstin": "1234",
# 		"taxable_value": 100,
# 		"ewaybill_serial_number": "2345677",
# 		"is_seller_registered_under_gst": False,
# 		"sgst_tax_rate": 100,
# 		"place_of_supply": "DELHI",
# 		"gst_discount": 0,
# 		"hsn_code": "1234",
# 		"sgst_amount": 100,
# 		"enterprise_gstin": "13",
# 		"gst_total_tax": 100,
# 		"igst_amount": 100,
# 		"cgst_amount": 200,
# 		"gst_tax_base": 200,
# 		"consignee_gstin": "1233",
# 		"igst_tax_rate": 100,
# 		"invoice_reference": "1234",
# 		"cgst_tax_rate": 100
# 	}
# }



#     response = requests.post(url, headers=headers)

#     print(response.text)
