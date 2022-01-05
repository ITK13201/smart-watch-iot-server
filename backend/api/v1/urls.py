from django.urls import path

from .gps.views import GpsAPIView
from .musics.views import MusicsAPIView
from .statuses.views import StatusesAPIView


urlpatterns = [
    path("gps", GpsAPIView.as_view(), name="api_v1_gps"),
    path("musics", MusicsAPIView.as_view(), name="api_v1_musics"),
    path("statuses", StatusesAPIView.as_view(), name="api_v1_statuses"),
]
