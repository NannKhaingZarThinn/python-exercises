ten_things = "Apples Oranges cows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix")

stuff = ten_things.split(' ')
more_stuff =  {"Day", "Night", "Song", "Firebee",
				"Corn", "Banana", "Girl", "Boy"}
while len(stuff) !=10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print (f"There are {len(stuff)} items n ow.")
	
print ("There we go : ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa! cool!
print (stuff.pop())
print (' '.join(stuff)) # what? cool !
print ('#'.join(stuff[3:5])) #super stealler!