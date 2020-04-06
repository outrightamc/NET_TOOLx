# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from napalm import get_network_driver
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html", {})