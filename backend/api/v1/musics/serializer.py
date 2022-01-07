import logging

from rest_framework import serializers

from musics.models import Music

logger = logging.getLogger(__name__)


class MusicsApiPOSTSerializer(serializers.Serializer):
    file_path = serializers.CharField(required=True)
    url = serializers.CharField(required=True)
    bpm = serializers.FloatField(required=True)
    length = serializers.FloatField(required=True)

    def save(self) -> Music:
        validated_data = self.validated_data
        logger.info(validated_data)

        music = Music(
            file_path=validated_data.get("file_path"),
            url=validated_data.get("url"),
            bpm=validated_data.get("bpm"),
            length=validated_data.get("length"),
        )
        music.save()

        return music
