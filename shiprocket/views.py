from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
import requests
import json
from shiprocket.authentication import get_shiprocket_token
from shiprocket.create_quick_order import create_quick_order

def get_tracking_details(tracking_id):
    token = get_shiprocket_token()
   
        
    url = "https://apiv2.shiprocket.in/v1/external/courier/track/shipment/16104408"
    # need to replace the url 16104408 which actual traking id

    payload={}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token["token"]} '
    }
   
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "something went wrong"



class TrackOrder(GenericAPIView):

    def get(self, request , *args, **kwargs):
        shipment_id = kwargs.get("shipment_id")
        result = get_tracking_details(shipment_id)
    
        return Response({"result":result },status=status.HTTP_200_OK)
    

        
# class CreateShipment(GenericAPIView): # there is no need of createing shipment it will be called after payment or cod mode

#     def post(self, request, *args, **kwargs):
#         result = create_quick_order(address="address of user", product_id="id of prduct")
#         return Response({"result": result}, status=status.HTTP_200_OKs)

