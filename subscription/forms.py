# -*- coding: utf-8 -*- 

from django import forms
from subscription.models import Subscription
# model for usa metaprogramação para gerar os campos apartir do modelo

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		exclude = ('created_at',) # not put this
