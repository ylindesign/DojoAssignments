from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=45)
	author = models.TextField(max_length=1000)
	category = models.CharField(max_length=45)
	dates = models.BooleanField(default=True)
	inprint = models.BooleanField(default=True)
	newprint = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)