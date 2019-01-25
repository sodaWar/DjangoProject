# -*- coding: utf-8 -*-

from django.http import HttpResponse

from mysql_test.models import Test


# 数据库操作
def insertdb(request):                                                                        # 添加数据
    test1 = Test(name='python')
    test2 = Test(name='java')
    test1.save()
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")

def searchdb(request):                                                                      # 查询数据
    result = ''
    list = Test.objects.all()
    for data in list:
        result += data.name + "   "
    return HttpResponse("<p>" + result + "</p>")

def updatedb(request):
    data = Test.objects.get(id=2)
    data.name = 'Google'
    data.save()
    # 另一种方式
    Test.objects.filter(id=2).update(name='Google')
    return HttpResponse("<p>数据修改成功！</p>")

def deletedb(request):
    data = Test.objects.get(id=2)
    data.delete()
    # 另一种方式
    Test.objects.filter(id=1).delete()