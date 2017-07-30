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
            "dream_audio_url": "sample_url",
            "content": "sample_content",
            "created_timestamp": datetime.now(),
            "updated_timestamp": datetime.now()
        }
        return Response(dummy_response, status=status.HTTP_200_OK)



    def get(self, request, *args, **kwargs):

        dummy_response = [
          {
            "dream_audio_url": "sample_url",
            "content": "sample_content",
            "created_timestamp": datetime.now(),
            "updated_timestamp": datetime.now()
          },
          {
            "dream_audio_url": "sample_url_2",
            "content": "sample_content_2",
            "created_timestamp": datetime.now(),
            "updated_timestamp": datetime.now()
          }
        ]
        return Response(dummy_response, status=status.HTTP_200_OK)


class DreamRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        dummy_response = {
            "dream_audio_url": "sample_url",
            "content": "sample_content",
            "created_timestamp": datetime.now(),
            "updated_timestamp": datetime.now()
        }
        return Response(dummy_response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        dummy_response = {
          "message": "success"
        }
        return Response(dummy_response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        dummy_response = {
            "dream_audio_url": "sample_url",
            "content": "sample_content",
            "created_timestamp": datetime.now(),
            "updated_timestamp": datetime.now()
        }
        return Response(dummy_response, status=status.HTTP_200_OK)
