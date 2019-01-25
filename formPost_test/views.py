# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserInfo


def index(request):
    form = UserInfo()                                                       # 创建对象
    if request.method == 'POST':
        data = UserInfo(request.POST)                                       # 将post过来的数据交给UserInfo类处理
        if data.is_valid():                                                 # 验证数据,数据合法则返回true
            print (data.clean())                                            # 打印前端传过来的具体数据值
            return HttpResponse('submit success and correct!!')
        else:
            print '1'
            form_error = form.errors                                        # 获取错误信息
            print form_error

    return render(request, 'index.html', {'form': form})


# Create your views here.
