from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = CharField(max_length=45)
	last_name = CharField(max_length=45)
	password = CharField(max_length=45)
	email = CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = userManager()

class userManager(models.Model):
	def addUser(self):
		
		return response

	def valUser(self):
		response = {}

		try:

