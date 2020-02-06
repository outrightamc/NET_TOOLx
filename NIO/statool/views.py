# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Device
from napalm import get_network_driver

def index(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    context = {
        'title' : 'NIO Statool - Main Dashboard',
        'owner' : 'NIO Team',
        'devices' : devices
    }
    return render(request, 'base.html', context)

def get_device_stats(request: HttpRequest, device_id) -> HttpResponse:
    device = Device.objects.get(pk=device_id)
    driver = get_network_driver(device.napalm_driver)
    with driver(device.host, device.username, device.password) as device_conn:
        interfaces = device_conn.get_interfaces()
    print(interfaces)
    return HttpResponse(f'{device_id}')

#Default view, before starting to configuring
#def get_devices(request: HttpRequest) -> HttpResponse:
#   pass
# comment
