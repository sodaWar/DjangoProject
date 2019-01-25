"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from formGet_test import views
# from formPost_test import views
# from azz_test import views
# from sendEmail_test import views
from mysql_test import testdb

urlpatterns = [
    # url(r'^testdb$',testdb.insertdb),
    # url(r'^testdb$',testdb.searchdb),
	url(r'^testdb$',testdb.updatedb),
	# url(r'^testdb$',testdb.deletedb),
	#url(r'^$',views.add2,name='add2'),
	#url(r'^$',views.home2,name='home2'),
	#url(r'^add/$',views.add,name='add'),
	#url(r'^jiafa/(\d+)/(\d+)/$',views.add2,name='add2'),
    # url(r'^search-form$', views.search_form),                               # formGet_test
    # url(r'^search$', views.search),                                         # formGet_test
    url(r'^admin/', admin.site.urls),
]
