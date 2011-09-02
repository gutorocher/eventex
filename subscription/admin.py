# -*- coding: utf-8 -*- 

import datetime
from django.contrib import admin
from subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name','cpf','email','phone','created_at', 
	'subscribed_today')

	def subscribed_today(self, obj):
		return obj.created_at.date()==datetime.date.today()
	subscribed_today.short description = 'Inscrito hoje?'


admin.site.register(Subscription, SubscriptionAdmin)
