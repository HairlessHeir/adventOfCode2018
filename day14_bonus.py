puzzleInput = "890691"
currentRecipes,currentIndexFirst,currentIndexSecond = "37",0,1
while True:
    currentRecipes += str(int(currentRecipes[currentIndexFirst]) + int(currentRecipes[currentIndexSecond]))
    currentIndexFirst = (currentIndexFirst+(int(currentRecipes[currentIndexFirst])+1))%(len(currentRecipes))
    currentIndexSecond = (currentIndexSecond+(int(currentRecipes[currentIndexSecond])+1))%(len(currentRecipes))
    if currentRecipes[-len(puzzleInput):] == puzzleInput:
        break

print(currentRecipes.find(str(puzzleInput)))



