# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

import random


def toss():
	heads = 0
	tails = 0
	for x in range(1,5001):
		random_num = random.random()
		rounded = round(random_num)
		if rounded == 1.0:
			heads += 1
			print "Attempt #", x, ": Throwing a coin... It's a head! .. got", heads, "head(s) so far and ", tails, "tail(s) so far"
		else:
			tails += 1
			print "Attempt #", x, ": Throwing a coin... It's a tail! .. got", heads, "head(s) so far and ", tails, "tail(s) so far"

toss()