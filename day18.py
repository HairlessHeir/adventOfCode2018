from collections import defaultdict
from copy import copy

def readFile(name):
    acres = defaultdict(lambda : 'x')
    i,j = 0,0
    with open(name) as f:
        i = 0
        for line in f.readlines():
            j = 0
            for el in list(line.rstrip()):
                acres[str(i)+":"+str(j)] = el
                j += 1
            i += 1
    return acres,i,j

def lumberyardGenerator(numOfMinutes,acresArray,sizeX,sizeY):
    for x in range(sizeX):
        for y in range(sizeY):
            print acresArray[str(x)+":"+str(y)],
        print
    print
    for i in range(numOfMinutes):
        temp = copy(acresArray)
        for x in range(sizeX):
            for y in range(sizeY):
                countLumberyards = 0
                countTrees = 0
                countOpens = 0
                changed = False
                for a in range(3):
                    for b in range(3):
                        if a == 1 and b == 1:
                            continue
                        if temp[str(x-1+a)+":"+str(y-1+b)] == '.':
                            countOpens += 1
                        elif temp[str(x-1+a)+":"+str(y-1+b)] == '#':
                            countLumberyards += 1
                        elif temp[str(x-1+a)+":"+str(y-1+b)] == '|':
                            countTrees += 1

                if countTrees >= 3 and not changed:
                    if temp[str(x)+":"+str(y)] == '.':
                        changed = True
                        acresArray[str(x)+":"+str(y)] = '|'
                if countLumberyards>=3 and not changed:
                    if temp[str(x)+":"+str(y)] == '|':
                        changed = True
                        acresArray[str(x)+":"+str(y)] = '#'
                if temp[str(x)+":"+str(y)] == '#' and not changed:
                    if countLumberyards>=1 and countTrees>=1:
                        changed = True
                        acresArray[str(x)+":"+str(y)] = '#'
                    else:
                        changed = True
                        acresArray[str(x)+":"+str(y)] = '.'
        totalCountLumber = 0
        totalCountWood = 0
        for x in range(sizeX):
            for y in range(sizeY):
                if acresArray[str(x)+":"+str(y)] == '#':
                    totalCountLumber += 1
                if acresArray[str(x)+":"+str(y)] == '|':
                    totalCountWood += 1
                print acresArray[str(x)+":"+str(y)],
            print
        print "SCORE", totalCountLumber, totalCountWood, totalCountLumber*totalCountWood
        print

                

        

acresArray,sizeX,sizeY = readFile("input18.txt")
lumberyardGenerator(10, acresArray,sizeX,sizeY)
