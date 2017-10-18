# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import render
from models import *

# Create your views here.
class OpinionListView(ListView):
    model = Opinion
    # template = "opinions/opinion_detail.html"

    def get_context_data(self, **kwargs):
        context = super(OpinionListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['opinions'] = Opinion.objects.all()
        return context

class OpinionDetailView(DetailView):
    model = Opinion

    def get_context_data(self, **kwargs):
        context = super(OpinionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def agreesWith(request,opinion_pk):
    opinion = Opinion.objects.get(pk=opinion_pk)
    if (opinion):
        opinion.agrees += 1

def disagreesWith(request,opinion_pk):
    opinion = Opinion.objects.get(pk=opinion_pk)
    if (opinion):
        opinion.disagrees += 1
