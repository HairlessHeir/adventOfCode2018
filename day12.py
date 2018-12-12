def readFile(filename):
    instructions = {}
    with open(filename) as f:
        initState = f.readline().split("state: ")[1].rstrip()
        f.readline()
        for line in f.readlines():
            instructions[line.split(" => ")[0]] = line.split(" => ")[1].rstrip()
    return initState,instructions

def runSimulation(initState,instructions,generations):
    for i in range(generations):
        print i

initialState, instructionSet = readFile("input12.txt")
runSimulation(initialState,instructionSet,20)
