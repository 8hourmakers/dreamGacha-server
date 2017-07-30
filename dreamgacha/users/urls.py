from django.conf.urls import url

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    )

urlpatterns = [
    url(r'^$', UserCreateAPIView.as_view(), name='create_user'),
    url(r'^auth/$', UserLoginAPIView.as_view(), name='login_user'),
]
