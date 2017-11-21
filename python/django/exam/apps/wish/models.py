from __future__ import unicode_literals

from django.db import models
from ..login.models import User


class wishManager(models.Manager):
	def Valid(self, new_wish):
		response = {}
		errors = []
		if len(new_wish) < 1:
			errors.append('Wishes cannot be blank!')
		if len(new_wish) < 4:
			errors.append('Wishes should be more than 3 characters')
		if errors:
			response['status'] = False
			response['errors'] = errors
		else:
			response['status'] = True
		return response

	def AddWish(self, new_wish, person):
		response = {}
		response['items'] = self.create(item=new_wish, user=person)
		response['items'].add.add(person)

	def CopyWish(self, id, person):
		# response = {}
		# response['items'] = self.get(id=id)
		# response['items'].add.add(person)
		thing = self.get(id=id)
		thing.add.add(person)
		# self.create(item=new_wish, add=person)

	def DeleteWish(self, id):
		# self.get(item=new_wish, user=person).delete()
		self.get(id=id).delete()

	def RemoveWish(self, id, person):
		# self.get(item=new_wish, user=person).delete()
		response = {}
		response['items'] = self.get(id=id)
		response['items'].add.remove(person)
		# self.get(item=new_wish).delete()

class Wish(models.Model):
	item = models.TextField()
	user = models.ForeignKey(User, related_name = 'user_wish')
	add = models.ManyToManyField(User, related_name = 'wished_by')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = wishManager()