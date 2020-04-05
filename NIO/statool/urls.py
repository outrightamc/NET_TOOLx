from django.conf.urls import url
#from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from .views import login

urlpatterns = [
# below line ('') will show default page for http://localhost:7777 requests
    path('', views.index),
    path('login/', login),
    path('devices/<int:device_id>', views.get_device_stats, name="device"),
]