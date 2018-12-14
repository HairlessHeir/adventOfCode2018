import numpy as np
import copy

def readFile(filename):
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            row = list(line.rstrip())
            rows.append(row)

    a = np.array([rows])
    return a

def printTracks(cartStage):
    print cartStage.shape
    for row in cartStage:
        print ' '.join(row)
def getNextPosition(x,y,cartType,cartStage):
    cartTypes = [">","v","<","^"]
    print cartStage
    print cartStage.shape
    if cartType == cartTypes[0]:
        if cartStage[x+1,y] == "\\":
            cartStage[x+1,y+1] = "v"
        elif cartStage[x,y+1] == "/":
            cartStage[x-1,y+1] = "^"
        elif cartStage[x+1,y] == "-":
            cartStage[x+1,y] = ">"
        elif cartStage[x+1,y] == "+":
            cartStage[x+1,y] = "^"
        cartStage[x,y] = "-"
    elif cartType == cartTypes[1]:
        if cartStage[x,y+1] == "\\":
            cartStage[x+1,y+1] = ">"
        elif cartStage[x,y+1] == "/":
            cartStage[x-1,y+1] = "<"
        elif cartStage[x,y+1] == "|":
            cartStage[x,y+1] = "v"
        elif cartStage[x,y+1] == "+":
            cartStage[x,y] = ">"
        cartStage[x,y] = "|"
    elif cartType == cartTypes[2]:
        if cartStage[x-1,y] == "\\":
            cartStage[x-1,y-1] = "^"
        elif cartStage[x-1,y] == "/":
            cartStage[x-1,y+1] = "v"
        elif cartStage[x-1,y] == "-":
            cartStage[x-1,y] = "<"
        elif cartStage[x-1,y] == "+":
            cartStage[x-1,y] = "v"
        cartStage[x,y] = "-"
    elif cartType == cartTypes[3]:
        if cartStage[x,y-1] == "\\":
            cartStage[x-1,y-1] = "<"
        elif cartStage[x,y-1] == "/":
            cartStage[x+1,y-1] = ">"
        elif cartStage[x,y-1] == "|":
            cartStage[x,y-1] = "^"
        elif cartStage[x,y-1] == "+":
            cartStage[x-1,y-1] = "<"
        cartStage[x,y] = "|"
    return cartStage


def getCartCrash(cartStage):
    cartTypes = [">","<","v","^"]
    while True:
        for i,row in enumerate(cartStage):
            for j,el in enumerate(row):
                if el in cartTypes:
                    cartStage = getNextPosition(i, j, el, cartStage)

        printTracks(cartStage)
    

getCartCrash(readFile("input13_test.txt"))
