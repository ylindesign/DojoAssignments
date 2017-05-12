mylist = ['magical unicorns', 'world']
integer = 0
sums = 0
string = ""
stringCount = 0

for x in mylist:
	if isinstance(x, int):
		sums += x
		integer += 1
	if isinstance(x, float):
		sums += x
		integer += 1
	elif isinstance(x, str):
		string += x
		string += " "
		stringCount += 1

if integer > 0 and stringCount == 0:
	print "The array you entered is of integer type"
	print "Sum :", sums
elif integer == 0 and stringCount > 0:
	print "The array you entered is of string type"
	print "String: ", string
elif integer > 0 and stringCount > 0:
	print "The array you entered is of mixed type"
	print "Sum :", sums
	print "String: ", string