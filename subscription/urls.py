# -*- coding: utf-8 -*- 
from django.conf.urls.defaults import patterns, include, url
from core.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from route import route

urlpatterns = patterns('subscription.view',
	route(r'^$', GET='new', POST ='create', name='subscribe'),
	url(r'^(\d+)/sucesso/$', 'sucess', name='sucess'),
)