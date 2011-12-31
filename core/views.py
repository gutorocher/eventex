# -*- coding: utf-8 -*- 
# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def homepage(request):

	context = { 'MEDIA_URL': settings.MEDIA_URL}
	
	return render_to_response('index.html', context)


