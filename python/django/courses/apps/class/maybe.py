# MODELS

# class createManager(models.Manager):
# 	def validate_post(self, secret):
# 		# if request.method == 'POST':
# 		# user = User.objects.create(content = secret.user_secret)
# 		errors = []

# 		if len(secret['user_secret.post_secret']) < 2:
# 			errors.append('secret is too short')
# 			response_to_views = {}

# 		if errors:
# 			response_to_views['status'] = False
# 			response_to_views['errors'] = errors
# 		else:
# 			# user = User.objects.get(id=secret['user_id'])
# 			response_to_views['status'] = True
# 			# response_to_views['user'] = user

# 		return response_to_views	

# POST Views
# if request.method == "POST":
		# response_from_models = Create.objects.validate_post(request.POST)
		# if response_from_models['status']:
		# 	pass
		# else:
		# 	for error in response_from_models['errors']:
		# 		messages.error(request, error)
		# if len(user_secret < 1):
		# 	errors = []
		# 	errors.append('secret is too short')
		# 	for error in response_from_models['errors']:
		# 		messages.error(request, error)
				# print errors
	# response = Create.objects.get(secret)

