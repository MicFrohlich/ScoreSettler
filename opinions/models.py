# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Opinion(models.Model):
    title = models.CharField(max_length=50)
    opinion = models.CharField(max_length=255,null=True)
    agrees = models.IntegerField(null=True,default=0)
    disagrees = models.IntegerField(null=True,default=0)

class OpinionGroup(models.Model):
    name = models.CharField(max_length=20)
    opinions = models.ManyToManyField(Opinion,related_name='opinions')
    
