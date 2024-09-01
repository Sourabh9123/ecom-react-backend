from rest_framework.generics import GenericAPIView
import requests
from rest_framework.response import Response




def get_location_by_ip(ip_address):
    if ip_address == "127.0.0.1":
        ip_address = "8.8.8.8"
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    if response.status_code == 200:
        data = response.json()
        location = data.get('loc')  # Format: 'latitude,longitude'
        latitude, longitude = location.split(',')  # Split into latitude and longitude
        print("inside location")
        return {
            'ip': data.get('ip'),
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country'),
            'latitude': latitude,
            'longitude': longitude,
        }
    else:
        return None




class MapView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        print("inside view")
        user_ip = request.META.get('REMOTE_ADDR')
        print(user_ip)
        # location_data = get_location_by_ip(user_ip)
        # print(location_data)
        # if location_data:
        #     return Response(location_data)
        # else:
        #     return Response({'error': 'Unable to get location'}, status=400)

        return None

