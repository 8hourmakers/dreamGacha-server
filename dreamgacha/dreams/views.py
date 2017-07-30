from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from rest_framework.generics import (
    ListCreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
    )
from rest_framework.permissions import (
    IsAuthenticated, AllowAny
)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


class DreamCreateListAPIView(APIView):
    permission_classes = [AllowAny]
    # serializer_class =

    def post(self, request, *args, **kwargs):

        dummy_response = {
            "id": 1,
            "title": "인형들이 나를 잡아먹었다",
            "dream_audio_url": "sample_url",
            "content": "곰돌이 인형이랑 토끼 인형이 나를 쫓아왔다.",
            "created_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return Response(dummy_response, status=status.HTTP_200_OK)



    def get(self, request, *args, **kwargs):

        dummy_response = [
          {
            "id": 1,
            "title": "인형들이 나를 잡아먹었다",
            "dream_audio_url": "sample_url",
            "content": "곰돌이 인형이랑 토끼 인형이 나를 쫓아왔다.",
            "created_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          },
          {
            "id": 1,
            "title": "인형들이 나를 잡아먹었다",
            "dream_audio_url": "sample_url_2",
            "content": "곰돌이 인형이랑 토끼 인형이 나를 쫓아왔다. 석주가 발을 걸어서 넘어져서 곰인형한테 잡아먹혔다.",
            "created_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          }
        ]
        return Response(dummy_response, status=status.HTTP_200_OK)


class DreamRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        dummy_response = {
            "id": 1,
            "title": "인형들이 나를 잡아먹었다",
            "dream_audio_url": "sample_url",
            "content": "곰돌이 인형이랑 토끼 인형이 나를 쫓아왔다.",
            "created_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return Response(dummy_response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        dummy_response = {
          "message": "success"
        }
        return Response(dummy_response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        dummy_response = {
            "id": 1,
            "title": "인형들이 나를 잡아먹었다",
            "dream_audio_url": "sample_url",
            "content": "곰돌이 인형이랑 토끼 인형이 나를 쫓아왔다.",
            "created_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return Response(dummy_response, status=status.HTTP_200_OK)
