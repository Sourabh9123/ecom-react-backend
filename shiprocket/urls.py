from django.urls import path
from shiprocket.views import TrackOrder

urlpatterns =  [
    path("track_delevery/<int:shipment_id>/",TrackOrder.as_view(), name="track-order" ),


]
