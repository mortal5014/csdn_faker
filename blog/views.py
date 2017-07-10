# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    title = "人工神经网络"
    nickname = "mortal"
    return render(request, 'index.html', locals())