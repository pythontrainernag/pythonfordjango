# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from module.models import sample
from module.forms import Sample as s

# Create your views here.

def m1(request):
    form_data = s()
    return render(request, "first.html", {'form': form_data})

def m2(request):
    d1 = sample.objects.all()
    return render(request, "second.html", {"data": d1})
