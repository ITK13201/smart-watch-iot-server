import logging
from typing import Optional

from rest_framework import serializers

from statuses.models import Status, STATUS_CHOICES

from django.core.validators import RegexValidator


logger = logging.getLogger(__name__)

STATUS_VALIDATOR = RegexValidator(
    regex="(inactive|active)", message='Status param must be "(inactive|active)"'
)


class StatusesApiPOSTSerializer(serializers.Serializer):
    status = serializers.CharField()

    def save(self) -> Status:
        validated_data = self.validated_data
        logger.info(validated_data)

        status_str = validated_data.get("status")

        status = Status(status=self.str2int_status(status_str))
        status.save()

        return status

    def str2int_status(self, status: str) -> Optional[int]:
        for choice in STATUS_CHOICES:
            if status == choice[1]:
                return choice[0]
        return None
