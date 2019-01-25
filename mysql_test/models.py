# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Test(models.Model):                                                           # 数据库中存储的表名为mysql_test_test,前面是app名字,test是类名
    name = models.CharField(max_length=30)


# Create your models here.
