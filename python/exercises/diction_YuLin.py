# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

# There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values.

# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.

data = {"Name": "Yu", "Age": "25", "Country": "Taiwan", "Lang": "HTML/CSS"}

def info():
	print "My name is ", data.get("Name")
	print "My age is ", data.get("Age")
	print "My country of birth is ", data.get("Country")
	print "My favorite language is ", data.get("Lang")

info()