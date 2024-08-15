from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import DHLService
from .serializers import ShipmentSerializer, TrackingSerializer

class CreateShipmentView(APIView):
    def post(self, request):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            dhl_service = DHLService()
            shipment_response = dhl_service.create_shipment(serializer.validated_data)
            print(shipment_response)
            return Response(shipment_response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackShipmentView(APIView):
    def post(self, request):
        serializer = TrackingSerializer(data=request.data)
        if serializer.is_valid():
            tracking_number = serializer.validated_data['tracking_number']
            dhl_service = DHLService()
            tracking_response = dhl_service.track_shipment(tracking_number)
            return Response(tracking_response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
