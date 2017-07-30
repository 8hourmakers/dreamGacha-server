import re
from datetime import date, timedelta

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
    IntegerField
)
from .models import User


class UserCreateSerializer(ModelSerializer):
    password = CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate_email(self, value):
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value

    def validate_password(self, value):
        if len(value) > 20 or not re.match('^([a-zA-Z0-9]{4,20})$', value):
            raise ValidationError("Invalid Password Format")
        return value

    def create(self, validated_data):
        # convert user_password to password
        validated_data['username'] = validated_data.get('email')
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(ModelSerializer):
    user_password = CharField(source='password', write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

