# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# A sample output would be like this:

# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

# Price: 2000
# Speed: 5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12

class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "Price: {}".format(self.price)
		print "Speed: {}".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {}".format(self.mileage)
		if self.price > 10000:
			self.tax = 0.15
		print "Tax: {}".format(self.tax)
		return self

car1 = Car(10000, "20mph", "Full", "4mpg")
car2 = Car(2000, "30mph", "Half", "5mpg")
car3 = Car(6000, "15mph", "Quarter", "10mpg")
car4 = Car(88800, "5mph", "Full", "8mpg")
car5 = Car(90050, "60mph", "Full", "25mpg")
car6 = Car(10, "10000mph", "Three-Quarters", "8mpg")
