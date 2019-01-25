# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def index(request):
    subject = 'test django send email'
    content = 'hei,this is django send email to you,thank you for watching!!'
    text_content = 'hei,this is a text format file'
    html_content = '<H1>this is a html format file</H1>'
    # send_mail(subject,content,'893026750@qq.com',['893026750@qq.com'],fail_silently=False)                              # 发送一条邮件,fail_silently值为false时，send_email将产生smtp.SMTPException异常

    # send_mail每次发送邮件都会建立一个连接,发送多个邮件就会建立多个连接;send_mass_mail是建立单个连接发送多封邮件
    # subject1 = 'test1 django send email'
    # subject2 = 'test2 django send email'
    # content1 = (subject1,content,'893026750@qq.com',['893026750@qq.com'])
    # content2 = (subject2,content,'893026750@qq.com',['893026750@qq.com'])
    # send_mass_mail((content1,content2),fail_silently=False)                                                             # 一次性发送多个邮件

    # 在发送的邮件中添加附件
    # from_email = settings.DEFAULT_FROM_EMAIL
    # msg = EmailMultiAlternatives(subject,content,from_email,['893026750@qq.com'])
    # msg.content_subtype = 'html'                                                                                        # 设置发送的内容为html格式
    # msg.attach_file('D:\MyProgram\PythonProject\PycharmProjects\python_practice\hool.txt')                              # 使用文件系统中的文件创建附件
    # msg.send()

    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['893026750@qq.com'])
    msg.attach_alternative(html_content,"text/html")                                                                    # 主类型是text,子类型是html,如果收件人可以处理html类型,则显示html类型
    msg.send()
    return HttpResponse('send email success')
# Create your views here.
