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
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from django.conf import settings
from .serializers import UserCreateSerializer
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
        request_data = request.data
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            res_data = {
                'token': str(token[0]),
                'email': user.email
            }
            return Response(res_data, status=status.HTTP_200_OK)
        if not User.objects.filter(email=request_data.get('email')).exists():
            return Response({'message': 'email duplicated'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'email duplicated'}, status=status.HTTP_404_NOT_FOUND)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        user = authenticate(username=data.get('email'), password=data.get('password'))
        if user is None:
            return Response(data={'message': 'wrong email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get_or_create(user=user)
        res_data = {
            'email': user.email,
            'token': str(token[0])
        }
        return Response(res_data, status=status.HTTP_200_OK)

        #
        # dummy_response = {
        #     "token": "dummytoken",
        #     "email": "sample_email_address"
        # }
        # return Response(dummy_response, status=status.HTTP_200_OK)
