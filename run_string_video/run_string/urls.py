from django.urls import path
from . import views

app_name = 'runtext'


urlpatterns = [
    path('runtext', views.send_video, name='send_video'),
]
