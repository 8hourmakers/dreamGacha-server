from django.conf.urls import include, url

urlpatterns = [
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^dreams/', include('dreams.urls', namespace='dreams')),

]

