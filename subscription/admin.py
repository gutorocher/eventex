#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Gus Rocha on 2011-08-28.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from django import admin
from subscription.models import Subscription
from django.contrib import admin

admin.site.register(Subscription)