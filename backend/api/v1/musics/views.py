import logging
import numpy as np

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.request import Request

from .serializer import MusicsApiPOSTSerializer
from fitbit_client.apiclient import FitbitApiClient
from fitbit_client.get_heart_rate import get_latest_heart_rate
from musics.models import Music

from django.forms.models import model_to_dict


logger = logging.getLogger(__name__)


HEART_RATE_ADDITION = 30


class MusicsAPIView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request) -> Response:
        heart_rate = self._get_mean_of_heart_rate()
        nearest_music = self._get_nearest_music(heart_rate)

        context = {
            "file_path": nearest_music["file_path"],
            "url": nearest_music["url"],
            "bpm": nearest_music["bpm"],
            "length": nearest_music["length"],
        }

        return Response(
            context,
            status=status.HTTP_200_OK,
        )

    def _get_mean_of_heart_rate(self) -> float:
        client = FitbitApiClient().initial()
        dataframe = get_latest_heart_rate(client)
        values = dataframe["value"]
        mean = sum(values) / len(values)
        return mean

    def _get_nearest_music(self, heart_rate: float) -> dict:
        musics = list(Music.objects.all().values())
        print(musics)
        bpm_list = [music["bpm"] for music in musics]
        idx = np.abs(np.asarray(bpm_list) - (heart_rate + HEART_RATE_ADDITION)).argmin()
        return musics[idx]

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = MusicsApiPOSTSerializer(data=data)
        if serializer.is_valid():
            music = serializer.save()
            music_dict = model_to_dict(music)
            logger.info(music_dict)

            return Response(
                music_dict,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
