from collections import defaultdict,namedtuple



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
    distances = {}
    minDistance = 1000000
    for i,coordinate in enumerate(coordinates):
        distances[i] = abs(coordinate[0]-currentPoint[0])+abs(coordinate[1]-currentPoint[1])
        if distances[i]<=minDistance:
            minDistance=distances[i]
    count = 0
    myKey = ""
    for key,value in zip(distances.keys(),distances.values()):
        if value == minDistance:
            count += 1
            myKey = key
    if count > 1:
        myKey = "."
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
    removeKeys = []
    areaSizes = defaultdict(lambda : 1)
    for i in range(maxValue+1):
        for j in range(maxValue+1):
            currentPoint = point(j,i)
            if currentPoint in coordinates:
                #print "+",
                counter += 1
            else:
                valueForCoordinate = getPointValue(coordinates,currentPoint)
                if i == 0 or i == maxValue or j == 0 or j == maxValue:
                	removeKeys.append(valueForCoordinate)
                
                areaSizes[valueForCoordinate]+=1
                #print valueForCoordinate,
    for el in removeKeys:
    	areaSizes[el] = 0
    maximumArea = 0
    for el2 in areaSizes.keys():
       	if int(areaSizes[el2])>maximumArea:
       		maximumArea = areaSizes[el2]
    print maximumArea

makeGrid(readFile())