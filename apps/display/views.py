# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import strftime, gmtime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "display/index.html", context)