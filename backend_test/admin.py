# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Article

class ArticleInfo(admin.ModelAdmin):
    list_display = ('title','content','pubish_time','update_time')                                                      # 把这个文章表里想要显示的值放进去
    search_fields = ('title','content','pubish_time','update_time')                                                     # 添加搜索功能

admin.site.register(Article,ArticleInfo)


# Register your models here.
