my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


newList = []
for x,y in my_dict.items():
	stuff = x,y
	newList.append(stuff) 

print newList