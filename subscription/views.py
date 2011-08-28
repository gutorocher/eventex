# -*- coding: utf-8 -*- 
# Create your views here.

from django.http import HttpResponseRedirect
from forms import SubscriptionForm
from reverse import reverse
from django.shortcuts import get_object_or_404

def new(request):
	
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subsdcription/new.html',context)


def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subsdcription/new.html',context)
	
	subsdcription = form.save()
	return HttpResponseRedirect(
		reverse ('subsdcription:sucess', args=[subsdcription.pl]))

def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else
		return new(request)

def sucess (request,pk)
	subscription = get_object_or_404(Subscription, pk=pk)
	context = RequestContext(request, {'subscription':subscription})
	return render_to_response('subscription/sucess.html',context)