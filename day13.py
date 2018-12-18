import numpy as np
import copy

class Cart:
    def __init__(self,cartType,x,y):
        self.cartType = cartType
        self.x = x
        self.y = y
        self.turnDirection = 0
    def turnDirection(self):
        return self.turnDirection
    def setTurnDirection(self):
        self.turnDirection += 1
        self.turnDirection %= 3
    def moveModifier(self):
        modX,modY = 0,0
        if self.cartType == "<":
            modX,modY = -1,0
        elif self.cartType == ">":
            modX,modY = 1,0
        elif self.cartType == "^":
            modX,modY = 0,-1
        elif self.cartType == "v":
            modX,modY = 0,1
        return modX,modY
    def angleRightMoveModifier(self):
        #for / angle
        modX,modY = 0,0
        if self.cartType == "<":
            modX,modY = -1,1
        elif self.cartType == ">":
            modX,modY = 1,-1
        elif self.cartType == "^":
            modX,modY = 1,-1
        elif self.cartType == "v":
            modX,modY = -1,1
        return modX,modY
    def angleLeftMoveModifier(self):
        #for \ angle
        modX,modY = 0,0
        if self.cartType == "<":
            modX,modY = -1,-1
        elif self.cartType == ">":
            modX,modY = 1,1
        elif self.cartType == "^":
            modX,modY = -1,-1
        elif self.cartType == "v":
            modX,modY = 1,1
        return modX,modY

def readFile(filename):
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            row = list(line.rstrip())
            rows.append(row)
    return rows

def cartDict(cartStage):
    cartTypes = [">","^","<","v"]
    carts = {}
    for i,row in enumerate(cartStage):
            for j,el in enumerate(row):
                if el in cartTypes:
                    carts[len(carts)+1] = Cart(el, i, j)
    for (k,cart) in carts.items():
        if cart.cartType == "<":
            cartStage[cart.x][cart.y] = "-"
        elif cart.cartType == ">":
            cartStage[cart.x][cart.y] = "-"
        elif cart.cartType == "^":
            cartStage[cart.x][cart.y] = "|"
        elif cart.cartType == "v":
            cartStage[cart.x][cart.y] = "|"

    return carts, cartStage

def printCarts(carts):
    for (k,v) in carts.items():
        print k,v.cartType,"(",v.x,",",v.y,")"

def printTracks(cartStage):
    for row in cartStage:
        print ' '.join(row)
def getNextPosition(cartStage,carts):
    cartTypes = [">","v","<","^"]
    cartCrash = False

    for (k,cart) in carts.items():
        modX,modY = cart.moveModifier()
        if cartStage[x+modX][y+modY] == "\\":
            lX,lY = cart.angleLeftMoveModifier()
            carts[k].x = cart.x+lX
            carts[k].y = cart.y+lY

        elif cartStage[x+modX][y+modY] == "/":
            cartStage[x-1][y+1] = "^"
        elif cartStage[x+modX][y+modY] == "-":
            cartStage[x+1][y] = ">"
        elif cartStage[x+modX][y+modY] == "+":
            cartStage[x+1][y] = "^"
        cartStage[x][y] = "-"

    return cartStage, cartCrash


def getCartCrash(cartStage):
    cartTypes = [">","<","v","^"]
    carts, cartStage = cartDict(cartStage)
    printCarts(carts)
    printTracks(cartStage)
    
    while True:
        cartStage,cartCrash = getNextPosition(cartStage, carts)
        printTracks(cartStage)
        if cartCrash:
            break
    

getCartCrash(readFile("input13_test.txt"))
