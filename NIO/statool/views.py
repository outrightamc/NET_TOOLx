# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Device, Service
from napalm import get_network_driver
from django.contrib.auth.decorators import login_required
import requests

# Page, with login to allow access the main/home page.
# when browsing to http://rasp:7777 URL
@login_required(login_url='/accounts/login/')
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


# Below is a redirectly to Statool APP 
# This is an entire new APP
@login_required(login_url='/accounts/login/')
def statool(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    services = Service.objects.all()
    context = {
        'title' : 'NIO Statool',
        'owner' : 'NIO Team',
        'devices' : devices,
        'services' : services
    }
# in below example, some "context" can be given to be used with the template,
# allowing easy customization of messages (remember the static blog posts from the video)
    return render(request, 'base.html', context)


# Below scripts redirect us to the "scripts.html" webpage
# when browsing to http://rasp:7777/statool URL
# ============
# Display and redirecto to Webpage
def scripts(request: HttpRequest) -> HttpResponse:
    return render(request, 'scripts.html')

# Give action to button, displaying info at the same page
# This button can redirect to another page.
def button(request):
    return render(request, 'scripts.html')

# Runs the script itself, getting the information from the website
def output(request):
    data=requests.get("https://xkcd.com/1906/")
    print(data.text)
    data=data.text
    return render(request, 'scripts.html' , {'data':data})

# ============

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
