from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from ..login.models import User

class secretManager(models.Manager):
	def Valid(self, secret_post):
		response = {}
		errors = []
		if len(secret_post) < 1:
			errors.append('Secret cannot be blank!')
		if errors:
			response['status'] = False
			response['errors'] = errors
		else:
			response['status'] = True
		return response

	def AddSecret(self, secret_post, person):
		self.create(content=secret_post['content'], user=person)

	def AddLike(self, user_id, secret_id):
		this_user = User.objects.get(id=user_id)
		this_secret = self.get(id=secret_id)
		like = this_secret.like.add(this_user)
		return True

	def CountLikes(self):
		# count = Secrets.objects.CountLikes
		# return count
		pass





class Secret(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, related_name = 'user_secret')
	likes = models.ManyToManyField(User, related_name = 'user_likes')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = secretManager()


