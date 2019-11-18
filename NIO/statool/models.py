# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    service_type = models.CharField(
        max_length=30, 
        choices=(('CCA_AMERICAS', 'hey'), ('CCA_APAC', 'hey1'), ('CCA_EMEA', 'hey3'))
    )

    def __str__(self) -> str:
        return self.name