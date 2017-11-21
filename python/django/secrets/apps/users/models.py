from __future__ import unicode_literals

from django.db import models

import re, md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

class userManager(models.Manager):
	def Regis(self, person):
		response = {}
		errors = []
		if len(person['first_name'])<2 or len(person['last_name']) < 2:
			errors.append('First & last name needs to be more than 2 characters')
		if len(person['email']) < 1:
			errors.append('Email cannot be blank!')
		if not EMAIL_REGEX.match(person['email']):
			errors.append('This email is invalid')
		if User.objects.filter(email = person['email']):
			errors.append('Email is taken!')		
		if len(person['password']) < 8:
			errors.append('Password must be longer than 8 characters')
		if not (person['password']) == (person['conf_pw']):
			errors.append('Passwords must match!')
		if errors:
			response['status'] = False
			response['errors'] = errors
		else:
			hashed_pw = md5.new(person['password']).hexdigest()
			print "hashed_pw at regis", hashed_pw
			response['status'] = True
			response['person'] = self.create(first_name=person['first_name'], last_name=person['last_name'], email=person['email'], password=hashed_pw,)
		return response

	def Valid(self, person):
		response = {}

		try:
			user = User.objects.get(email=person['email'])

			login_hash = md5.new(person['password']).hexdigest()
			print "login hash:", login_hash
			print "user password:", user.password
			print "user first_name:", user.first_name
			print "user last_name:", user.last_name

			if user.password == login_hash:
				response['status']= True
				response['user']= user
				response['email']=email
				return response
			else:
				response ['status'] = False
				return response
		except:
			pass
			# response ['status'] = False
			# return response


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = userManager()
		