class Animal(object):
	"""docstring for Animal"""
	def __init__(self, names):
		self.names = names
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "{}: {} health remaining".format(self.names, self.health)
		return self

animal1 = Animal("bird")
# animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, names):
		super(Dog, self).__init__(names)
		self.health = 150	
	def pet(self):
		self.health += 5
		return self

dog1 = Dog("dog")	

# dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, names):
		super(Dragon, self).__init__(names)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print "this is a dragon!"
		super(Dragon, self).displayHealth()
		return self

dragon1 = Dragon("dragon")

# dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()

bird = Animal("chicken")

bird.walk().displayHealth()	

