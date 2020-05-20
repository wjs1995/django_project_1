# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from test1.models import Test


def hello(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("成功了兄嘚")