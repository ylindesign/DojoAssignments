# class MathDojo(object):
# 	"""docstring for MathDojo"""
# 	def __init__(self):
# 		super(MathDojo, self).__init__()
# 		self.num1 = 0
# 	def add(self, int1, *intA):
# 		if intA:
# 			self.num1 += int1 + intA[0]
# 		else:
# 			self.num1 += int1
# 		return self
# 	def subtract(self, int2, *intB):
# 		if intB:
# 			self.num1 -= (int2 + intB[0])
# 		else:
# 			self.num1 -= int2
# 		return self
# 	def result(self):
# 		print self.num1

class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		super(MathDojo, self).__init__()
		self.num1 = 0
	def add(self, *intA):
		if intA:
			# self.num1 += int1
			for x in xrange(0,len(intA)):
				if isinstance(intA[x], list):
					for y in intA[x]:
						# print y
						self.num1 += y
				else:
					self.num1 += intA[x]
		else:
			self.num1 += int1
		return self
	def subtract(self, int2, *intB):
		if intB:
			self.num1 -= (int2 + intB[0])
		else:
			self.num1 -= int2
		return self
	def result(self):
		print self.num1

# md = MathDojo().add(2).add(2, 5).subtract(3, 2).result()

md2 = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25],(5, 8)).result()



