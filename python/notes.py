# Python

# Dictionaries

weekend = {"Sun": "Sunday", "Mon": "Monday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data

# Built-in Functions and Methods
Python includes the following standalone functions for dictionaries:

cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the 2 dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.
Python includes the following dictionary methods:
(either dict.method(yourDictionary) or yourDictionary.method() will work)

.clear() - removes all elements from the dictionary
.copy() - returns a shallow copy dictionary
.fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
.get(key, default=None) - For key key, returns value or default if key is not in dictionary.
.has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
.items() - returns a list of dictionary's (key, value) tuple pairs.
.keys() - return a list of dictionary keys.
.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
.update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
.values() - returns list of dictionary values.

Nested Dictionaries
Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples.

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }
Copy
To iterate the values, we can use the nested for loop:

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"
Copy
The result is like this...

Question # 1 :  Why is there a light in the fridge and not in the freezer?
----
Question # 2 :  Why don't sheep shrink when it rains?
----
Question # 3 :  Why are they called apartments when they are all stuck together?
----
Question # 4 :  Why do cars drive on the parkway and park on the driveway?
----


Lists from Dictionary
It's possible to create lists from dictionaries by using the methods items(), keys() and values(). As the name implies the method keys() creates a list, which consists solely of the keys of the dictionary. While values() produces a list consisting of the values. items() can be used to create a list consisting of 2-tuples of (key, value)-pairs:

data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']
Copy
Dictionaries from Lists
For example, we have two lists, one containing the dishes and the other, the corresponding countries:

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
Copy
Now we will create a dictionary, which assigns a dish to a country (of course according to the common prejudices). For this purpose, we need the function zip(). The name zip was well chosen because the two lists get combined like a zipper.

country_specialities = zip(countries, dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
Copy
The variable country_specialities now contains the "dictionary" in the 2-tuple list form. This form can be easily transformed into a real dictionary with the function dict().

country_specialities_dict = dict(country_specialities)
print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}
Copy
There is still one question concerning the function zip(). What happens, if one of the two argument lists contains more elements than the other one? It's easy: The superfluous elements will not be used, whether the extras are keys or values:

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
Copy
Notice Switzerland is dropped from the set of keys.
