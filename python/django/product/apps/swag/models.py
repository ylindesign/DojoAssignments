from __future__ import unicode_literals

from django.db import models

class Stuff(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField(max_length=1000)
	weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	category = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)