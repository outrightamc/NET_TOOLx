from django.conf.urls import url
#from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

from . import views
from accounts.views import login_view

urlpatterns = [
# Below line ('') will show default page for http://localhost:7777 requests
# The following paths (routes) like "statool/" and "devices" were created to
# forward request based on what was configured in "views.py" file, adding the 
# .statool name

    path('', views.home, name='network-tools-home'),
    path('statool/', views.statool, name='statool-home'),
    path('devices/<int:device_id>', views.get_device_stats, name="device"),
]
