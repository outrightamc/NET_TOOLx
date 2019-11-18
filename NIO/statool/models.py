# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.Charfield(max_lenght=100)
    name = models.Charfield(max_lenght=70)
    username = models.Charfield(max_lenght=100)
    password = models.Charfield(max_lenght=70)
    service_type = models.Charfield(choices=['CCA AMERICAS', 'CCA APAC', 'CCA EMEA'])
