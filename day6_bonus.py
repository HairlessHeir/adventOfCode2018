from collections import defaultdict,namedtuple



point = namedtuple("point",["x","y"])

def readFile(fileName):
	coordinates = []
	with open(fileName) as f:
		for line in f.readlines():
			coordinate = line.split(", ")
			coordinates.append(point(int(coordinate[0]),int(coordinate[1])))
	return coordinates

def getPointValue(coordinates,currentPoint):
    totalDistance = 0
    maximumDistance = 10000

    for i,coordinate in enumerate(coordinates):
        totalDistance += abs(coordinate[0]-currentPoint[0])+abs(coordinate[1]-currentPoint[1])

    myKey = "."
    if totalDistance < maximumDistance:
    	myKey = "#"

    return myKey

def makeGrid(coordinates):
    maxV = 0
    maxH = 0
    for coordinate in coordinates:
        if coordinate.x>maxH:
            maxH=coordinate.x
        if coordinate.y>maxV:
            maxV=coordinate.y

    maxValue = int(max([maxH,maxV]))
    counter = 0
    totalArea = 0
    removeKeys = []
    areaSizes = defaultdict(lambda : 1)
    for i in range(maxValue+1):
        for j in range(maxValue+1):
            currentPoint = point(j,i)
            if currentPoint in coordinates:
                valueForCurrent = getPointValue(coordinates,currentPoint)
                if valueForCurrent == "#":
                	totalArea += 1
                counter += 1
            else:
                valueForCurrent = getPointValue(coordinates,currentPoint)
                if valueForCurrent == "#":
                	totalArea += 1
    print totalArea

    # for el in removeKeys:
    # 	areaSizes[el] = 0
    # maximumArea = 0
    # for el2 in areaSizes.keys():
    #    	if int(areaSizes[el2])>maximumArea:
    #    		maximumArea = areaSizes[el2]
    # print maximumArea

makeGrid(readFile("input6.txt"))