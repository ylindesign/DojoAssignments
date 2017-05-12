name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  new_dict = {}
  temp = zip(arr1, arr2)
  for x, y in temp:
  	new_dict[x] = y
  return new_dict

print make_dict(name, favorite_animal)