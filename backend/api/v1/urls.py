from django.urls import path

from .gps.views import GpsAPIView
from .musics.views import MusicAPIView


urlpatterns = [
    path("gps", GpsAPIView.as_view(), name="api_v1_gps"),
    path("musics", MusicAPIView.as_view(), name="api_v1_musics"),
]
