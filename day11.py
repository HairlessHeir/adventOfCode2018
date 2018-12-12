def cellPowerLevel(x,y,serNum):
    return int(((x+10)*y+serNum)*(x+10)/100)%10-5

def maxPowerCellCoordinate(serNum):
    powerGrid = {}
    for i in range(1,301):
        for j in range(1,301):
            powerGrid[i,j] = cellPowerLevel(i,j,serNum)

    myX,myY = 0,0
    maxPower = 0
    for i in range(1,299):
        for j in range(1,299):
            currentPowerSquare = 0
            for k in range(3):
                for l in range(3):
                    currentPowerSquare+=powerGrid[i+k,j+l]
            if currentPowerSquare>maxPower:
                maxPower = currentPowerSquare
                myX = i
                myY = j
    print "(",myX,myY,") : ",maxPower
##
maxPowerCellCoordinate(7315)
