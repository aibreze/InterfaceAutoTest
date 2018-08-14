# -*- coding: UTF-8 -*-
"""
@author:Duan jun ming
@file: urls.py
@time: 2018/08/06
qq:1032241157
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from InterfaceTestManage import views

urlpatterns = [
   url('^index$',views.getIndex),
   url('^welcome$',views.welcome),
   url('^login$',views.login),
   url('^register$',views.reigster),
]
