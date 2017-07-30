from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from django.conf import settings

User = get_user_model()
# from .models import PRUsUserMaster
# from .serializers import UserCreateSerializer, UserLoginSerializer, UserSelfDetailSerializer, \
#     UserEmailSerializer, UserSearchPasswordSerializer, PRUsUserMasterSerializer
# from .auth.token import get_or_create_token, delete_token
from django.db import transaction

"""
model = PRUsUserMaster
        fields = ('user_no', 'user_password', 'passport_no', 'mobile_phone_no',
                  'home_phone_no', 'control_remarks')
"""


class UserCreateAPIView(APIView):
    """회원가입 API View
    """
    permission_classes = [AllowAny]
    # serializer_class = UserCreateSerializer

    def post(self, request, format=None):
        dummy_response = {
            "token": "dummytoken",
            "email": "sample_email_address"
        }
        return Response(dummy_response, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        dummy_response = {
            "token": "dummytoken",
            "email": "sample_email_address"
        }
        return Response(dummy_response, status=status.HTTP_200_OK)
