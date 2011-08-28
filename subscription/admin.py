# -*- coding: utf-8 -*- 

from django.contrib import admin
from subscription.models import Subscription


class Subscription(admin.ModelAdmin):
	list_display = ('nome','cpf','email','phone','created_at')

admin.site.register(Subscription, SubscriptionAdmin)
