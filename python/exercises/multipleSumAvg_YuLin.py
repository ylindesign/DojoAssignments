# Multiples
for x in xrange(1,1000): # Prints all odd numbers from 1 to 1000
	if x % 2 == 1:
		print x

for y in xrange(1,1000000): # Prints all multiples of 5 from 5 to 1000000
	if y % 5 == 0:
		print y

# Sum List
a = [1, 2, 5, 10, 255, 3]
b = sum(a) # Sums up all the values in the list a
print b

# Average List
c = sum(a)/len(a)
print c