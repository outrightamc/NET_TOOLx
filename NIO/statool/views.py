# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to StaTool</h1>")