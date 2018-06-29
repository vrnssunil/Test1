# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Testcalc(models.Model):
    number = models.IntegerField()
    square =  models.IntegerField()
