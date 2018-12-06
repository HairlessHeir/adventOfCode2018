from collections import defaultdict

def readFile():
	coordinates = []
	with open("input6.txt") as f:
		for line in f.readlines():
			coordinate = line.split(", ")
			coordinates.append((int(coordinate[0]),int(coordinate[1])))
	return coordinates

def getClosest(coordinates, point):
	coordinate = point.split(":")

def makeGrid(coordinates):
	grid = {}
	minH,maxH,minV,maxV = 1000,0,1000,0
	for pair in coordinates:
		grid[str(pair[0])+":"+str(pair[1])] = "0"
		if minH > pair[0]:
			minH = pair[0]
		if maxH < pair[0]:
			maxH = pair[0]
		if minV > pair[1]:
			minV = pair[1]
		if maxV < pair[1]:
			maxV = pair[1]	

	counter = 1
	for i in range(maxH-minH+1):
		for j in range(maxV-minV+1):
			grid[str(i+minH)+":"+str(j+minV)] = counter
	for key in grid.keys():
		result = getClosest(coordinates,key)
	print grid

makeGrid(readFile())