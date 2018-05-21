from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.registers, name='registers'),
#    url(r'^responseform/$', views.checkresponse, name='checkresponse'),
    url(r'^alert/$', views.alert, name='alert'),
]
