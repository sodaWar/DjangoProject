# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-07 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('age', models.IntegerField(verbose_name='\u5e74\u9f84')),
                ('phone', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='\u4e66\u540d')),
                ('publication_time', models.DateField(verbose_name='\u51fa\u7248\u65f6\u95f4')),
                ('author', models.ManyToManyField(to='book_sys.Author', verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u4e66\u540d',
                'verbose_name_plural': '\u4e66\u540d',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u51fa\u7248\u793e')),
                ('address', models.CharField(max_length=50, verbose_name='\u51fa\u7248\u793e\u5730\u5740')),
                ('city', models.CharField(max_length=30, verbose_name='\u57ce\u5e02')),
                ('province', models.CharField(max_length=30, verbose_name='\u7701\u4efd')),
                ('country', models.CharField(max_length=30, verbose_name='\u56fd\u5bb6')),
                ('website', models.URLField(verbose_name='\u5b98\u7f51')),
            ],
            options={
                'verbose_name': '\u51fa\u7248\u793e',
                'verbose_name_plural': '\u51fa\u7248\u793e',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_sys.Publisher', verbose_name='\u51fa\u7248\u793e'),
        ),
    ]