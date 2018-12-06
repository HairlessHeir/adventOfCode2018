from collections import defaultdict,namedtuple
from math import hypot



point = namedtuple("point",["x","y"])

def readFile():
	coordinates = []
	with open("input6.txt") as f:
		for line in f.readlines():
			coordinate = line.split(", ")
			coordinates.append(point(int(coordinate[0]),int(coordinate[1])))
	return coordinates

#distance = hypot(current[0]-coordinate[0],current[1]-coordinate[1])

def getPointValue(coordinates,currentPoint):
	for i,coordinate in enumerate(coordinates):
		distances[i] = hypot(coordinate[0]-currentPoint[0],coordinate[1]-currentPoint[1])

def makeGrid(coordinates):
	maxV = 0
	maxH = 0
	for coordinate in coordinates:
		if coordinate.x>maxH:
			maxH=coordinate.x
		if coordinate.y>maxV:
			maxV=coordinate.y
	counter = 0
	for i in range(maxH):
		for j in range(maxV):
			currentPoint = point(i,j)
			if currentPoint in coordinates:
				print counter,
				counter += 1
			else:
				valueForCoordinate = getPointValue(coordinates,currentPoint)
				print ".",
		print

makeGrid(readFile())