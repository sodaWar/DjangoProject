# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#	return HttpResponse(u'welcome to study django!')

#def index(request):
#	string = u'study django'
#	return render(request,'home.html',{'string':string})

def index(request):
    return render(request, 'add2.html')

def home(request):
	mylist = ['HTML','CSS','Python','Java','PHP']
	return render(request,'home.html',{'mylist':mylist})
	
def home2(request):
	mydict = {'site':u'tony','content':u'study java'}
	return render(request,'home2.html',{'mydict':mydict})

#def add(request):
#	a = request.GET.get('a',0)
#	b = request.GET.get('b',0)
#	c = int(a)+int(b)
#	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))


# Create your views here.
