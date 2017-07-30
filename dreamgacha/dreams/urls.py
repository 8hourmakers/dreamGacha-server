from django.conf.urls import url

from .views import (
    DreamCreateListAPIView,
    DreamRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    url(r'^$', DreamCreateListAPIView.as_view(), name='create_list_dream'),
    url(r'^(?P<dream_id>[0-9]+)/$', DreamRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_dream')
]
