# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def search_form(request):
    return render(request,'two.html')

def search(request):
    if 'query' in request.GET:
        message = '你搜索的内容为：'+ request.GET['query']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# Create your views here.
