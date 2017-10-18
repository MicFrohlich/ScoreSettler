# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    template = "templates/opinions/index.html"
    return render(request,template)
