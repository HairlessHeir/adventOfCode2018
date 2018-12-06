from collections import defaultdict
from math import hypot

def readFile():
	coordinates = []
	with open("input6.txt") as f:
		for line in f.readlines():
			coordinate = line.split(", ")
			coordinates.append((int(coordinate[0]),int(coordinate[1])))
	return coordinates

def getClosest(coordinates, point):
	coordinate = (int(point.split(":")[0]),int(point.split(":")[1]))
	minDistance = 10000
	closestPoints = 0
	for current in coordinates:
		distance = math.hypot(current[0]-coordinate[0],current[1]-coordinate[1])
		if distance <= minDistance:
			minDistance = distance
			closestPoints += 1
	if closestPoints >

def makeGrid(coordinates):
	grid = {}
	minH,maxH,minV,maxV = 1000,0,1000,0
	counter = 0
	for pair in coordinates:
		grid[str(pair[0])+":"+str(pair[1])] = counter
		counter += 1
		if minH > pair[0]:
			minH = pair[0]
		if maxH < pair[0]:
			maxH = pair[0]
		if minV > pair[1]:
			minV = pair[1]
		if maxV < pair[1]:
			maxV = pair[1]	

	for i in range(maxH-minH+1):
		for j in range(maxV-minV+1):
			point = str(i+minH)+":"+str(j+minV)
			grid[point] = getClosest(coordinates, point)
	print grid

makeGrid(readFile())