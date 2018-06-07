animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals [0]
print (bear)

animals.append("kangaroo")
animals.append("whale")
animals.append("platypus")
animals.append("Ant")
animals.append("cat")

for ani in animals:
	print (f"All animals are : {ani}")

i = 0
for anim in animals:
	print (f"The first {i}st animal is at {i} and is a", anim)
	print (f"The animal at {i} is the {i}st animal and is a", anim)
	i += 1