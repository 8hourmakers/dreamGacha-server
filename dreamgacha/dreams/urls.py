from django.conf.urls import url

from .views import (
    DreamCreateListAPIView,
    DreamRetrieveUpdateDestroyAPIView,
    DreamAudioCreateAPIView,
    simple_upload,

    )

urlpatterns = [
    url(r'^simple_upload$', simple_upload, name='uploaded_file_url'),
    url(r'^audio/$', DreamAudioCreateAPIView.as_view(), name='uploaded_file_url'),
    url(r'^$', DreamCreateListAPIView.as_view(), name='create_list_dream'),
    url(r'^(?P<dream_id>[0-9]+)/$', DreamRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_dream')
]
