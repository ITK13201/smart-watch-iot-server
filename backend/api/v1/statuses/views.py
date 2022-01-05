import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.request import Request

from statuses.models import Status
from .serializer import StatusesApiPOSTSerializer

from django.forms.models import model_to_dict


logger = logging.getLogger(__name__)


class StatusesAPIView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request) -> Response:
        status_model = self.search()
        context = {"status": status_model.get_status_display()}
        logger.info(context)

        return Response(
            context,
            status=status.HTTP_200_OK,
        )

    def search(self) -> Status:
        statuses = Status.objects.filter().order_by("-created_at")[:1]
        status = statuses[0]

        return status

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = StatusesApiPOSTSerializer(data=data)
        if serializer.is_valid():
            status_model = serializer.save()
            status_dict = model_to_dict(status_model)
            logger.info(status_dict)

            return Response(
                status_dict,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
