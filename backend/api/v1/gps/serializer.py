import logging

from rest_framework import serializers

from gps.models import TRIGGER_TYPE_CHOICES, Gps


logger = logging.getLogger(__name__)


class GpsApiSerializer(serializers.Serializer):
    occurred_at = serializers.DateTimeField(
        input_formats=["iso-8601", "%B %d, %Y at %I:%M%p"], required=True
    )
    location_map_image_url = serializers.CharField(required=False)
    location_map_url = serializers.CharField(required=False)
    entered_or_exited = serializers.CharField(required=True)

    def save(self) -> Gps:
        validated_data = self.validated_data
        logger.info(validated_data)

        trigger_type = self._get_trigger_type(validated_data.get("entered_or_exited"))

        gps = Gps(
            occurred_at=validated_data.get("occurred_at"),
            location_map_image_url=validated_data.get("location_map_image_url"),
            location_map_url=validated_data.get("location_map_url"),
            trigger_type=trigger_type,
        )
        gps.save()

        return gps

    def _get_trigger_type(self, entered_or_exited: str):
        for choice in TRIGGER_TYPE_CHOICES:
            if entered_or_exited == choice[1]:
                return choice[0]
