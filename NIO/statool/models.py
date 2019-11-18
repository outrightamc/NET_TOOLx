# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_lenght=100)
    name = models.CharField(max_lenght=70)
    username = models.CharField(max_lenght=100)
    password = models.CharField(max_lenght=70)
    service_type = models.Charfield(
        max_lenght=30, choices=(('CCA AM', "CCA AMERICAS"), ('CCA AP', 'CCA APAC'), ('CCA EM', 'CCA EMEA') blank=True
    )
