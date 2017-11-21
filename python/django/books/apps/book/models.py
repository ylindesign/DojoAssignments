from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=45)
	author = models.TextField(max_length=1000)
	dates = models.DateField("Date*")
	category = models.CharField(max_length=45)
	inprint = models.BooleanField()
	newprint = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)