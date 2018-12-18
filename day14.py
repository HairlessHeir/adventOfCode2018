def getRecipes(recipes,indxOne,indxTwo):
    result = recipes[indxOne] + recipes[indxTwo]
    newRecipes = map(int,str(result))
    for i in newRecipes:
        recipes.append(i)
    indxOne = (indxOne+(recipes[indxOne]+1))%(len(recipes))
    indxTwo = (indxTwo+(recipes[indxTwo]+1))%(len(recipes))
    return recipes,indxOne,indxTwo

###
puzzleInput = 890691
currentRecipes,currentIndexFirst,currentIndexSecond = [3,7],0,1
numOfIterations = 900000
while True:
    currentRecipes,currentIndexFirst,currentIndexSecond = getRecipes(currentRecipes,currentIndexFirst,currentIndexSecond)
    numOfIterations -=1
    if numOfIterations <= 0:
        break
recipeOffset = puzzleInput
finalScore = ""
for i in currentRecipes[recipeOffset:recipeOffset+10]:
    finalScore += str(i)
print finalScore



