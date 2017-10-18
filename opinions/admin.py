# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from opinions.models import Opinion

# Register your models here.
class OpinionAdmin(admin.ModelAdmin):
    fields = ['title','opinion','agrees','disagrees']

admin.site.register(Opinion, OpinionAdmin)
