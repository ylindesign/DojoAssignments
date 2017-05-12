# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product class should have these attributes:
# Price
# Item Name
# Weight
# Brand
# Cost
# Status: default "for sale"
# Product class should have these methods:
# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
	"""docstring for Product"""
	def __init__(self, price, itemName, weight, brand, cost):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self
	def tax(self, tax):
		self.price += self.price * tax
		return self
	def returned(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.cost = 0
		elif reason == "box, like new":
			self.status = "for sale"
		elif reason == "box, opened":
			self.status = "used"
			self.price -= self.price * 0.2
		return self
	def display_info(self):
		print "Price: {}".format(self.price)
		print "Item Name: {}".format(self.itemName)
		print "Weight: {}".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Cost: {}".format(self.cost)
		print "Status: {}".format(self.status)


Product1 = Product(10000, "Soap", 20, "Prada", 5)
Product1.sell().display_info()