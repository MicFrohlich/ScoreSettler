# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render
from models import *

# Create your views here.
class OpinonListView(ListView):
    model = Opinion

def index(request):
    template = "opinions/opinion_view.html"
    return render(request,template)
