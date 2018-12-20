from collections import Counter
def instructionCounterImproved(instruction,valuesBefore,valuesAfter):
    opcodes = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    i1,i2,i3 = instruction[1],instruction[2],instruction[3]
    count = 0
    instructionList = []
    for opcode in opcodes:
        temp = valuesBefore[:]
        if opcode == "addr":
            temp[i3] = valuesBefore[i1] + valuesBefore[i2]
        elif opcode == "addi":
            temp[i3] = valuesBefore[i1] + i2
        elif opcode == "mulr":
            temp[i3] = valuesBefore[i1] * valuesBefore[i2]
        elif opcode == "muli":
            temp[i3] = valuesBefore[i1] * i2
        elif opcode == "banr":
            temp[i3] = valuesBefore[i1] & valuesBefore[i2]
        elif opcode == "bani":
            temp[i3] = valuesBefore[i1] & i2
        elif opcode == "borr":
            temp[i3] = valuesBefore[i1] | valuesBefore[i2]
        elif opcode == "bori":
            temp[i3] = valuesBefore[i1] | i2
        elif opcode == "setr":
            temp[i3] = valuesBefore[i1]
        elif opcode == "seti":
            temp[i3] = i1
        elif opcode == "gtir":
            if i1 > valuesBefore[i2]:
                temp[i3] = 1
            else:
                temp[i3] = 0
        elif opcode == "gtri":
            if valuesBefore[i1] > i2:
                temp[i3] = 1
            else:
                temp[i3] = 0
        elif opcode == "gtrr":
            if valuesBefore[i1] > valuesBefore[i2]:
                temp[i3] = 1
            else:
                temp[i3] = 0
        elif opcode == "eqir":
            if i1 == valuesBefore[i2]:
                temp[i3] = 1
            else:
                temp[i3] = 0
        elif opcode == "eqri":
            if i2 == valuesBefore[i1]:
                temp[i3] = 1
            else:
                temp[i3] = 0
        elif opcode == "eqrr":
            if valuesBefore[i1] == valuesBefore[i2]:
                temp[i3] = 1 
            else:
                temp[i3] = 0

        
        shouldCount = True
        for i,j in zip(temp,valuesAfter):
            if i!=j:
                shouldCount = False
                break
        if shouldCount:
            instructionList.append(opcode)
            count += 1
        temp = []
    return count,instructionList

def applyInstruction(opcode,oldRegister,instruction):
    opcodes = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    newRegister = oldRegister[:]
    i1,i2,i3 = instruction[1],instruction[2],instruction[3]

    if opcode == "addr":
        newRegister[i3] = oldRegister[i1] + oldRegister[i2]
    elif opcode == "addi":
        newRegister[i3] = oldRegister[i1] + i2
    elif opcode == "mulr":
        newRegister[i3] = oldRegister[i1] * oldRegister[i2]
    elif opcode == "muli":
        newRegister[i3] = oldRegister[i1] * i2
    elif opcode == "banr":
        newRegister[i3] = oldRegister[i1] & oldRegister[i2]
    elif opcode == "bani":
        newRegister[i3] = oldRegister[i1] & i2
    elif opcode == "borr":
        newRegister[i3] = oldRegister[i1] | oldRegister[i2]
    elif opcode == "bori":
        newRegister[i3] = oldRegister[i1] | i2
    elif opcode == "setr":
        newRegister[i3] = oldRegister[i1]
    elif opcode == "seti":
        newRegister[i3] = i1
    elif opcode == "gtir":
        if i1 > oldRegister[i2]:
            newRegister[i3] = 1
        else:
            newRegister[i3] = 0
    elif opcode == "gtri":
        if oldRegister[i1] > i2:
            newRegister[i3] = 1
        else:
            newRegister[i3] = 0
    elif opcode == "gtrr":
        if oldRegister[i1] > oldRegister[i2]:
            newRegister[i3] = 1
        else:
            temp[i3] = 0
    elif opcode == "eqir":
        if i1 == oldRegister[i2]:
            newRegister[i3] = 1
        else:
            newRegister[i3] = 0
    elif opcode == "eqri":
        if i2 == oldRegister[i1]:
            newRegister[i3] = 1
        else:
            newRegister[i3] = 0
    elif opcode == "eqrr":
        if oldRegister[i1] == oldRegister[i2]:
            newRegister[i3] = 1 
        else:
            newRegister[i3] = 0
    return newRegister
def solveRegisters(name,allInst):
    initialRegister = [0,0,0,0]
    with open(name) as f:
        for line in f.readlines():
            currentInstruction = (map(int,list(line.rstrip().split(" "))))
            initialRegister = applyInstruction(allInst[currentInstruction[0]], initialRegister,currentInstruction)[:]
    print initialRegister

def solveInstructions(name):
    allInstructionsFinal = {}
    with open(name) as f:
        lineCounter = 0
        instGroup = []
        allInstructions = {}
        for i in range(16):
            allInstructions[i] = Counter()
        for line in f.readlines():
            if lineCounter < 3:
                if lineCounter == 1:
                    instGroup.append(map(int,list(line.rstrip().split(" "))))
                else:
                    instGroup.append(map(int,list(line.rstrip().split("[")[1].split("]")[0].replace(" ","").split(",")))) 
                lineCounter += 1
            elif lineCounter == 3:
                instCount,instList = instructionCounterImproved(instGroup[1], instGroup[0], instGroup[2])
                allInstructions[instGroup[1][0]].update(instList)
                lineCounter = 0
                instGroup = []

        allInstructionsSet = {}
        for i in range(16):
            allInstructionsSet[i] = set(allInstructions[i])

        while len(allInstructionsFinal) < 16:
            for (k,v) in allInstructionsSet.items():
                if len(v) == 1:
                    allInstructionsFinal[k] = v.pop()
            for (k,v) in allInstructionsFinal.items():
                for i in range(16):
                    if v in allInstructionsSet[i]:
                        allInstructionsSet[i].remove(v)
    return allInstructionsFinal

allInst = solveInstructions("input16.txt")
solveRegisters("input16_bonus.txt", allInst)

