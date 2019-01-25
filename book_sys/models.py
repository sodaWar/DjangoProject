# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='出版社')
    address = models.CharField(max_length=50,verbose_name='出版社地址')
    city = models.CharField(max_length=30, verbose_name='城市')
    province = models.CharField(max_length=30, verbose_name='省份')
    country = models.CharField(max_length=30, verbose_name='国家')
    website = models.URLField(verbose_name='官网')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = '出版社'

class Book(models.Model):
    name = models.CharField(max_length=60, verbose_name='书名')
    author = models.ManyToManyField(Author,verbose_name='作者')
    publisher = models.ForeignKey(Publisher,verbose_name='出版社')
    publication_time = models.DateField(verbose_name='出版时间')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '书名'
        verbose_name_plural = '书名'



# Create your models here.
