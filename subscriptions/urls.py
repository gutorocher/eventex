# -*- coding: utf-8 -*- 

from django.conf.urls.defaults import patterns,url
#from route import route #route.py deve ficar dentro diretório eventex

urlpatterns = patterns('subscriptions.views',
	#route(r'^$', GET='new', POST='create', name='subscribe')
    url(r'^$','subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)