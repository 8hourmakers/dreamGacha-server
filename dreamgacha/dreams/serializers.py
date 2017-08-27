import re
from datetime import date, timedelta

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
    IntegerField
)
from .models import Dream


class DreamSerializer(ModelSerializer):

    class Meta:
        model = Dream
        fields = ('id', 'dream_audio_url', 'title', 'content', 'owner', 'created_timestamp', 'updated_timestamp')
        read_only_fields = ('id', 'owner', 'created_timestamp', 'updated_timestamp')

    def create(self, validate_date):
        request_user = self.context.get('request').user
        dream = Dream(
            dream_audio_url=validate_date.get('dream_audio_url'),
            title=validate_date.get('title'),
            content=validate_date.get('content'),
            owner=request_user
        )
        dream.save()
        return dream
