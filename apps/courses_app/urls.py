from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^destroyCourse/(?P<id>\d+)$', views.destroyCourse),
]