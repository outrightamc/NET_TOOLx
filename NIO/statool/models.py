# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=100)
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    service_type = models.Charfield(
        max_length=30, choices=(("AM", "CCA AMERICAS"), ("AP", "CCA APAC"), ("EM", "CCA EMEA")
    )
