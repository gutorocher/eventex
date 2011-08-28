#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Gus Rocha on 2011-08-28.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from django import admin
from subscription.models import Subscription

class Subscription(admin.ModelAdmin):
	list_display = ('nome','email','phone','created_at')

admin.site.register(Subscription, SubscriptionAdmin)