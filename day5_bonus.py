import string

def readFile():
	polymer = ""
	with open("input5.txt") as f:
		polymer = f.readlines()
	return polymer

def destroyPolymer(polymer):
	unitsList = []
	for upper,lower in zip(string.ascii_uppercase,string.ascii_lowercase):
		unitsList.append(upper+lower)
		unitsList.append(lower+upper)
	canDestroy = True
	while canDestroy:
		temp = polymer[0]
		for unit in unitsList:
			polymer[0] = polymer[0].replace(unit,"")
		if polymer[0] == temp:
			canDestroy = False
	return len(polymer[0])

def shortenAndDestroyPolymer(polymer):
	temp = polymer[0]
	mimimalSize = len(polymer[0])
	for upper,lower in zip(string.ascii_uppercase,string.ascii_lowercase):
		polymer[0] = polymer[0].replace(upper,"")
		polymer[0] = polymer[0].replace(lower,"")
		result = destroyPolymer(polymer)
		if result < mimimalSize:
			mimimalSize = result
		polymer[0] = temp
	print mimimalSize
####
shortenAndDestroyPolymer(readFile())