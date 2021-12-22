from django.urls import path

from .gps.views import GpsAPIView


urlpatterns = [path("gps", GpsAPIView.as_view(), name="api_v1_gps")]
