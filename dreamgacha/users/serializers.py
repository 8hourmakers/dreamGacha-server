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
    email_address = EmailField(label='Email Address')
    birthday = CharField(label='birthday', required=False)
    is_email_receive = BooleanField()
    is_sms_receive = BooleanField()
    user_password = CharField(source='password', write_only=True)

    class Meta:
        model = UsUserMaster
        fields = ('user_no', 'name', 'birthday', 'email_address', 'is_email_receive', 'email_receive_accept_time',
                  'user_password', 'gender', 'mobile_phone_no', 'is_sms_receive', 'sms_receive_accept_time')
        read_only_fields = ('user_no', 'email_receive_accept_time', 'sms_receive_accept_time')

    def validate_email_address(self, value):
        user_qs = UsUserMaster.objects.filter(email_address=value)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value

    def validate_mobile_phone_no(self, value):
        value = validate_korea_mobile_phone_no(value)
        user_qs = UsUserMaster.objects.filter(mobile_phone_no=value)
        if user_qs.exists():
            raise ValidationError("This mobile phone number is already registered.")
        return value

    def validate_birthday(self, value):
        birthday = validate_birthday_str(value)
        # 만 14세 미만 가입 금지
        age = (date.today() - birthday.date()) // timedelta(days=365.2425)
        if age < 14:
            return ValidationError("만 14세 미만은 가입할 수 없습니다.")
        return birthday

    def validate_user_password(self, value):
        if len(value) > 20 or not re.match('^([a-zA-Z0-9]{4,20})$', value):
            raise ValidationError("비밀번호 포맷이 잘못되었습니다.")
        return value

    def create(self, validated_data):
        # convert user_password to password
        user = UsUserMaster.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(ModelSerializer):
    user_password = CharField(source='password', write_only=True)

    class Meta:
        model = UsUserMaster
        fields = ('name', 'birthday', 'email_address', 'is_email_receive', 'email_receive_accept_time',
                  'user_password', 'gender', 'mobile_phone_no', 'is_sms_receive', 'sms_receive_accept_time')
        read_only_fields = ('email_receive_accept_time', 'sms_receive_accept_time')

