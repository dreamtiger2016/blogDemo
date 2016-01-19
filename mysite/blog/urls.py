#-*- coding: UTF-8 -*-   
from django.conf.urls import patterns, url
from .views import archive
from . import views
 
urlpatterns = patterns('',
        url(r'^$',archive),
        url(r'^login/$',views.login,name = 'login'),
        url(r'^regist/$',views.regist,name = 'regist'),
        url(r'^index/$',views.index,name = 'index'),
                      )