
from collections import defaultdict

def readFile():	
	lines = []
	with open("input3.txt") as f:
		lines = f.readlines()
	return lines

def cutFabric():
	fabric = defaultdict(lambda : 0)
	for line in inputLines:
		fabricPosition = line.split("@")[1].split(":")[0]
		fabricSize = line.split("@")[1].split(":")[1]
		i = int(fabricPosition.split(",")[0])
		j = int(fabricPosition.split(",")[1])
		for k in range(int(fabricSize.split("x")[0])):
			for l in range(int(fabricSize.split("x")[1])):
				fabric[str(i+k)+","+str(j+l)] += 1
	return fabric

def multipleClaimCounter(myFabric):
	total = 0
	for value in myFabric.values():
		if value > 1:
			total += 1
	return total


inputLines = readFile()
fabric = cutFabric()
print multipleClaimCounter(fabric)


