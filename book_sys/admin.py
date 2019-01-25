# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Author,Book,Publisher

class AuthorShow(admin.ModelAdmin):
    list_display = ('name','age','phone','email')                       # 展示的字段信息
    search_fields = ('name','age','phone','email')                      # 添加搜索功能
    fields = ('name','age','email','phone')                             # 编辑信息时显示的顺序
    ordering = ('age',)                                                 # 按照年龄排序,值必须是list或tuple
    list_filter = ('name',)                                             # 过滤器,页面会出现相应的过滤器选项

class BookShow(admin.ModelAdmin):
    raw_id_fields = ('author','publisher',)
    list_display = ('name','publisher','publication_time',)

admin.site.register(Author,AuthorShow)
admin.site.register(Book,BookShow)
admin.site.register(Publisher)

# Register your models here.
