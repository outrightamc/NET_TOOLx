from django.conf.urls import url
#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    url('', views.index),
#    url('devices', views.get_devices),
    url('devices/<int:device_id>', views.get_device_stats, name="device"),
]