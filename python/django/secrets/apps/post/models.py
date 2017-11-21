from __future__ import unicode_literals

from django.db import models
from ..users.models import User

class Create(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, related_name = 'user_secret')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# objects = createManager()