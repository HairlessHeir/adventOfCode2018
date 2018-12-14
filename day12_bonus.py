from collections import defaultdict

def readFile(filename):
    instructions = {}
    with open(filename) as f:
        initState = f.readline().split("state: ")[1].rstrip()
        initStateDict = defaultdict(lambda:".")
        for i,state in enumerate(initState):
                initStateDict[i] = state
        f.readline()
        instructions = defaultdict(lambda:".")
        for line in f.readlines():
            instructions[line.split(" => ")[0]] = line.split(" => ")[1].rstrip()

    return initStateDict,instructions

def runSimulation(initState,instructions,generations):
    minLeftIndex = 0
    maxRightIndex = len(initState)
    for i in range(generations):
        newPotValues = defaultdict(lambda:".")
        genString = ""
        for j in range(1,5):
            initState[min(initState.keys())-j] = "."
            initState[max(initState.keys())+j] = "."
        for (k,v) in initState.items():
            newPotValues[k] = instructions[initState[k-2]+initState[k-1]+initState[k]+initState[k+1]+initState[k+2]]
        
        for k in range(maxRightIndex+200):
            genString+=initState[k]    
        totalSum = 0

        for (k,v) in newPotValues.items():
            initState[k] = v
        for (k,v) in initState.items():
            if v == "#":
                totalSum+= k+50000000000-103
        newPotValues.clear()
    print totalSum

initialState, instructionSet = readFile("input12.txt")
runSimulation(initialState,instructionSet,103)
