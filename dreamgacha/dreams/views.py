import os
import subprocess
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
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .speech_to_text import stt
from .serializers import DreamSerializer
from .models import Dream
from config.pagination import Pagination30

def check_duration_time(filepath):
    duration = subprocess.check_output(['ffmpeg', '-i', str(filepath)])
    print(duration)

def simple_upload(request):
    """
    ffmpeg -i 5.m4a -ac 1 -ar 44100 5.wav
    :param request:
    :return:
    """
    if request.method == 'POST' and request.FILES.get('file'):
        myfile = request.FILES.get('file')
        if myfile is None:
            return render(request, 'web/simple_upload.html', {
                'messages': [
                    '파일이 비어있습니다!!'
                ]
            })
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        wav_filename = filename.split('.')[0] + '.wav'
        origin_file_ext = filename.split('.')[-1]
        if origin_file_ext not in ['wav', 'm4a', 'mp3', 'amr']:
            return render(request, 'web/simple_upload.html', {
                'uploaded_file_url': '',
                'stt_result': 'Invalid Format'
            })
        origin_file_path = os.path.join(fs.location, filename)
        destination_file_path = os.path.join(fs.location, wav_filename)

        subprocess.check_output(['ffmpeg', '-i', str(origin_file_path), '-ac', '1', '-ar', '44100', destination_file_path])
        stt_result = stt(os.path.join(fs.location, destination_file_path))
        print('stt_result', stt_result)
        uploaded_file_url = fs.url(filename)
        return render(request, 'web/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'stt_result': stt_result
        })
    return render(request, 'web/simple_upload.html')

class DreamAudioCreateAPIView(APIView):
    """
    ffmpeg -i 3.wav 2>&1 | grep Duration | awk '{print $2}' | tr -d ,
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('file')
        if not audio_file:
            return Response({'message': 'audio file required'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        wav_filename = filename.split('.')[0] + '.wav'
        origin_file_ext = filename.split('.')[-1]
        # Check Audio format
        if origin_file_ext not in ['wav', 'm4a', 'mp3', 'amr']:
            return Response({'message': 'invalid format'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        origin_file_path = os.path.join(fs.location, filename)
        destination_file_path = os.path.join(fs.location, wav_filename)

        subprocess.check_output(
            ['ffmpeg', '-i', str(origin_file_path), '-ac', '1', '-ar', '44100', destination_file_path])
        stt_result = stt(os.path.join(fs.location, destination_file_path))
        # Check stt recognize results
        if not stt_result:
            return Response({'message': 'cannot recognize'}, status=status.HTTP_400_BAD_REQUEST)
        uploaded_file_url = fs.url(filename)
        payload = {
            'dream_audio_url': uploaded_file_url,
            'content': stt_result
        }
        return Response(payload, status=status.HTTP_200_OK)


class DreamCreateListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DreamSerializer
    pagination_class = Pagination30

    def post(self, request, *args, **kwargs):
        """
        {
          "dream_audio_url": string <음성 URL>,
          "title": string <꿈 제목>,
          "content": string <꿈 텍스트 컨텐츠>
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = DreamSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



    def get(self, request, *args, **kwargs):
        queryset_list = Dream.objects.filter(owner=request.user).\
            order_by('-created_timestamp')
        if request.GET.get('start_id') is not None:
            queryset_list = queryset_list.filter(id__gt=request.GET.get('start_id'))
        serializer = DreamSerializer(queryset_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DreamRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DreamSerializer

    def put(self, request, dream_id, *args, **kwargs):
        dream = Dream.objects.filter(id=dream_id).first()
        if not dream:
            return Response({'message': 'dream id {} not exists'.format(str(dream_id))},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = DreamSerializer(dream, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'message': 'invalid input'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, dream_id, *args, **kwargs):
        dream_queryset = Dream.objects.filter(id=dream_id)
        if not dream_queryset.exists():
            return Response({'message': 'dream id {} not exists'.format(str(dream_id))}, status=status.HTTP_404_NOT_FOUND)
        dream_queryset.delete()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    def get(self, request, dream_id, *args, **kwargs):
        dream = Dream.objects.filter(id=dream_id).first()
        if not dream:
            return Response({'message': 'dream id {} not exists'.format(str(dream_id))},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = DreamSerializer(dream)
        return Response(serializer.data, status=status.HTTP_200_OK)
