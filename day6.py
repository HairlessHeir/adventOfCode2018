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
	closestPoints = []
	closestID = 0
	for i,current in enumerate(coordinates):
		distance = hypot(current[0]-coordinate[0],current[1]-coordinate[1])
		if distance <= minDistance:
			minDistance = distance
			closestPoints.append(current)
			closestID = str(i)

	if len(closestPoints) > 1:
		closestID = "."
	return closestID


def makeGrid(coordinates):
	grid = {}
	minH,maxH,minV,maxV = 1000,0,1000,0
	for i,pair in enumerate(coordinates):
		grid[str(pair[0])+":"+str(pair[1])] = str(i)
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
	for value in grid.values():
		print value

makeGrid(readFile())