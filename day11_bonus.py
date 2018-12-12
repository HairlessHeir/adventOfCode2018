import numpy as np

def cellPowerLevel(x,y,serNum):
    return int(((x+10)*y+serNum)*(x+10)/100)%10-5

def maxPowerCellCoordinate(serNum):
    powerGrid = {}
    myX,myY,mySize = 0,0,0
    maxPower = 0
    powerGridArray = np.zeros((300,300))
    for i in range(0,300):
        for j in range(0,300):
            powerGridArray[i,j] = cellPowerLevel(i,j,serNum)

    for squareSize in range(1,300):
        for i in range(0,300-squareSize):
            for j in range(0,300-squareSize):
                newSum = powerGridArray[i:i+squareSize,j:j+squareSize].sum()
                if newSum > maxPower:
                    maxPower = newSum
                    myX,myY,mySize = i,j,squareSize


    print "(",myX,myY,mySize,") : ",maxPower
##
maxPowerCellCoordinate(7315)
