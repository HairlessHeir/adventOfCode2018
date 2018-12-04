
from collections import defaultdict
from collections import namedtuple 

def readFile():	
	lines = []
	with open("input3.txt") as f:
		lines = f.readlines()
	return lines

def parseLine(boxData):
	parsedLine = namedtuple("boxInfo",["ID","position","size"])
	return parsedLine(boxData.split("@")[0].strip(),boxData.split("@")[1].split(":")[0].strip(),boxData.split("@")[1].split(":")[1].strip())

def specialFabric():
	fabric = defaultdict(lambda : 0)
	fabrics = []
	for line in inputLines:
		boxData = parseLine(line)
		fabrics.append(boxData.ID)
		i = int(boxData.position.split(",")[0])
		j = int(boxData.position.split(",")[1])
		for k in range(int(boxData.size.split("x")[0])):
			for l in range(int(boxData.size.split("x")[1])):
				fabric[str(i+k)+","+str(j+l)] += 1
				
	for line in inputLines:
		boxData = parseLine(line)
		i = int(boxData.position.split(",")[0])
		j = int(boxData.position.split(",")[1])
		shouldBreak = False
		for k in range(int(boxData.size.split("x")[0])):
			for l in range(int(boxData.size.split("x")[1])):
				if fabric[str(i+k)+","+str(j+l)] > 1:
					fabrics.remove(boxData.ID)
					shouldBreak = True
					break
			if shouldBreak:
				break

	return fabrics


inputLines = readFile()
for boxID in specialFabric():
	print boxID


