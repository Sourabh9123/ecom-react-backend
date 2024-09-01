from django.urls import  path
from map.views import MapView


urlpatterns = [
    path("location/", MapView.as_view(),name="" )
]
