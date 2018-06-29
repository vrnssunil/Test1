# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Testcalc
# Register your models here.
class Testdetail(admin.ModelAdmin):
    list_display = ('number','square')
admin.site.register(Testcalc,Testdetail)
