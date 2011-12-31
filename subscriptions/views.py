# -*- coding: utf-8 -*- 
# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import SubscriptionForm
from models import Subscription
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings


def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscriptions/new.html',context)
 

def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscriptions/new.html',context)
	
	
	subscription = form.save()
	#notifica o cadastro
	send_subscription_email(subscription)
	return HttpResponseRedirect(reverse ('subscriptions:success', args=[subsdcription.pk]))


def success (request, pk):
	subscriptions = get_object_or_404(Subscription, pk=pk)
	# VERY IMPORTANT READ DOCUMENTATION get_object_or_404
	context = RequestContext(request, {'subscriptions':subscription})
	return render_to_response('subscriptions/success.html',context)
	
