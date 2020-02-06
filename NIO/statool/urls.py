from django.conf.urls import url
#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('devices/<int:device_id>', views.get_device_stats, name="device"),
]