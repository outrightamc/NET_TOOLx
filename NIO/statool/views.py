# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Device
from napalm import get_network_driver
from django.contrib.auth.decorators import login_required

# Page, with login to allow access the main page.
# This is an entire new APP
@login_required(login_url='/accounts/login/')
def home(request: HttpRequest) -> HttpResponse:
#   The below is a simple message displayed using HttpResponse method    
#   return HttpResponse('<h1>Network Tools Home</h1>')

# Return message below redirects directly to home.html (not statool APP) 
# when you browse to http://rasp:7777 URL
    return render(request, 'home.html')


# Below is an old definition that send us directly to Statool APP 
# when browsing to http://rasp:7777 URL
@login_required(login_url='/accounts/login/')
def statool(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    context = {
        'title' : 'NIO Statool',
        'owner' : 'NIO Team',
        'devices' : devices
    }
# in below example, some "context" can be given to be used with the template,
# allowing easy customization of messages (remember the static blog posts from the video)
    return render(request, 'base.html', context)



def get_device_stats(request: HttpRequest, device_id) -> HttpResponse:
    device = Device.objects.get(pk=device_id)
    driver = get_network_driver(device.napalm_driver)
    with driver(device.host, device.username, device.password) as device_conn:
        interfaces = device_conn.get_interfaces()
        ipaddress = device_conn.get_interfaces_ip()
    context = {
        'device':device,
        'interfaces':interfaces,
        'ipaddress':ipaddress,
    }
    print(interfaces)
    print(ipaddress)
#    You can enable this when you want to see the debug on the terminal and read fields
    return render(request, 'device.html', context)

#Default view, before starting to configuring
#def get_devices(request: HttpRequest) -> HttpResponse:
#   pass
# comment
