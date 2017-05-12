# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D 
# Score: 70 - 79; Grade - C 
# Score: 80 - 89; Grade - B 
# Score: 90 - 100; Grade - A

import random
random_num = random.randint(60, 100)

def score():
	if random_num in range(60,70):
		print "Score: ", random_num, "; Your grade is D"
	elif random_num in range(70,80):
		print "Score: ", random_num, "; Your grade is C"
	elif random_num in range(80,90):
		print "Score: ", random_num, "; Your grade is B"
	elif random_num in range(90,100):
		print "Score: ", random_num, "; Your grade is A"

score()