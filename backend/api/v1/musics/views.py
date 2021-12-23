import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.request import Request

from .serializer import MusicApiPOSTSerializer

from django.forms.models import model_to_dict


logger = logging.getLogger(__name__)


class MusicAPIView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = MusicApiPOSTSerializer(data=data)
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
