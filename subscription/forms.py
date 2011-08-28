#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Gus Rocha on 2011-08-28.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

from django import forms
from subscription.models import Subscription

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		exclude = ('created_at',)
