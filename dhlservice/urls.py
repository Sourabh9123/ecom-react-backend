from django.urls import path
from .views import CreateShipmentView, TrackShipmentView

urlpatterns = [
    path('create-shipment/', CreateShipmentView.as_view(), name='create-shipment'),
    path('track-shipment/', TrackShipmentView.as_view(), name='track-shipment'),
]
