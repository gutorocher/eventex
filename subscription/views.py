# -*- coding: utf-8 -*- 
# Create your views here.

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from subscription.forms import SubscriptionForm
from subscription.models import Subscription


def new(request):
	
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html',context)
 

def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscription/new.html',context)
	
	
	subscription = form.save()
	#notifica o cadastro
	send_subscription_email(subscription)
	return HttpResponseRedirect(
		reverse ('subscription:success', args=[subsdcription.pk]))


def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)


def success (request,pk):
	subscription = get_object_or_404(Subscription, pk=id)
	# VERY IMPORTANT READ DOCUMENTATION get_object_or_404
	context = RequestContext(request, {'subscription':subscription})
	return render_to_response('subscription/success.html',context)
	
