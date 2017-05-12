# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
# def oddEven():
# 	for x in xrange(1,2001):
# 		if x % 2 == 0:
# 			print "Number is ", x, ". This is an even number."
# 		else:
# 			print "Number is ", x, ". This is an odd number."

# oddEven()


# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
arr = [2,4,5]
new_array = []

def multiply(array, int):
	for x in range( len(array) ):
		array[x] = array[x] * int
	return arr

# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def layered_multiples(arr):
	# print arr
	for x in arr:
		val_arr = []
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array

# layered_multiples(arr)

x = layered_multiples(multiply([2,4,5],3))
print x