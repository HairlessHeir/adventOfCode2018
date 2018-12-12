from collections import namedtuple
def readFile(filename):
    pointList = []
    with open(filename) as f:
        for line in f.readlines():
            positionNums = line.split("> velocity=<")[0].split("<")[1].split(",")
            velocityNums = line.split("> velocity=<")[1].split(">")[0].split(",")

            pointList.append([int(positionNums[0]),int(positionNums[1]),int(velocityNums[0]),int(velocityNums[1])])
    return pointList

def printMessage(points,xL,xR,yU,yD):
    print xL,xR,yU,yD
    for i in range(yU,yD+10):
        for j in range(xL,xR+10):
            if [j,i] in points:
                print "#",
            else:
                print ".",
        print

points = readFile("input10.txt")

totalTime = 0
distance = 120
while True:
    pointsForPrinting = []
    maxX,maxY = 0,0
    minX = points[0][0]
    minY = points[0][1]
    for i,singlePoint in enumerate(points):
        points[i][0]+=singlePoint[2]
        points[i][1]+=singlePoint[3]

        if points[i][0]>maxX:
            maxX=points[i][0]
        if points[i][0]<minX:
            minX=points[i][0]
        if points[i][1]>maxY:
            maxY=points[i][1]
        if points[i][1]<minY:
            minY=points[i][1]

        pointsForPrinting.append([points[i][0],points[i][1]])
    if maxX-minX<distance and maxY-minY<distance:
        printMessage(pointsForPrinting,minX,maxX,minY,maxY)
        print totalTime
    totalTime += 1

    if totalTime > 11000:
        break
