from collections import defaultdict

def readFile(filename):
    instructions = {}
    with open(filename) as f:
        initState = f.readline().split("state: ")[1].rstrip()
        initStateDict = defaultdict(lambda:".")
        for i,state in enumerate(initState):
                initStateDict[i] = state
        f.readline()
        for line in f.readlines():
            instructions[line.split(" => ")[0]] = line.split(" => ")[1].rstrip()
    return initStateDict,instructions

def runSimulation(initState,instructions,generations):
    minLeftIndex = 0
    maxRightIndex = len(initState.keys())
    for i in range(generations):
        newPotValues = []
        for k in range(len(initState.keys())):
            j = minLeftIndex+k
            potKey = initState[j-2]+initState[j-1]+initState[j]+initState[j+1]+initState[j+2]
            newPotValue = instructions[potKey]
            #print potKey," -> ",newPotValue
            newPotValues.append(newPotValue)
        totalSum = 0
        for k in range(len(newPotValues)):
            initState[minLeftIndex + k] = newPotValues.pop(0)
            print initState[minLeftIndex+k],
            if initState[minLeftIndex + k] == "#":
                totalSum+=minLeftIndex + k
        print "Gen:",i," sum:",totalSum
        print initState

        minLeftIndex -= 2
        maxRightIndex += 2

initialState, instructionSet = readFile("input12_test.txt")
runSimulation(initialState,instructionSet,3)
