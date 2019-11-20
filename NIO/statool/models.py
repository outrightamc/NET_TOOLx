# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    device_type = models.CharField(
        max_length=30, 
        choices=(('router', 'Router'), ('switch', 'Switch'), ('firewall', 'Firewall'))
    )
    platform = models.CharField(
        max_length=30, 
        choices=(('cisco', 'Cisco IOS'), ('junos', 'JUNOS'))
    )

    def __str__(self) -> str:
        return self.name