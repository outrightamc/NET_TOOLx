# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Device

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    context = {
        'title' : 'NIO Statool - Main Dashboard',
        'owner' : 'NIO Team',
        'devices' : devices
    }
    return render(request, 'base.html', context)

def get_devices(request: HttpRequest) -> HttpResponse:
    pass 