def instructionCounter(instruction,valuesBefore,valuesAfter):
    opcodes = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    #b0,b1,b2,b3 = valuesBefore[0],valuesBefore[1],valuesBefore[2],valuesBefore[3]
    #a0,a1,a2,a3 = valuesAfter[0],valuesAfter[1],valuesAfter[2],valuesAfter[3]
    i1,i2,i3 = instruction[1],instruction[2],instruction[3]
    count = 0
    print instruction," : ",valuesBefore," - >",valuesAfter
    for opcode in opcodes:
        if opcode == "addr":
            if valuesAfter[i3] == valuesBefore[i1] + valuesBefore[i2]:
                print "addr"
                count += 1
        elif opcode == "addi":
            if valuesAfter[i3] == valuesBefore[i1] + i2:
                print "addi"
                count += 1
        elif opcode == "mulr":
            if valuesAfter[i3] == valuesBefore[i1] * valuesBefore[i2]:
                print "mulr"
                count += 1
        elif opcode == "muli":
            if valuesAfter[i3] == valuesBefore[i1] * i2:
                print "muli"
                count += 1
        elif opcode == "banr":
            if valuesAfter[i3] == valuesBefore[i1] & valuesBefore[i2]:
                print "banr"
                count += 1
        elif opcode == "bani":
            if valuesAfter[i3] == valuesBefore[i1] & i2:
                print "bani"
                count += 1
        elif opcode == "borr":
            if valuesAfter[i3] == valuesBefore[i1] | valuesBefore[i2]:
                print "borr"
                count += 1
        elif opcode == "bori":
            if valuesAfter[i3] == valuesBefore[i1] | i2:
                print "bori"
                count += 1
        elif opcode == "setr":
            if valuesAfter[i3] == valuesBefore[i1]:
                print "setr"
                count += 1
        elif opcode == "seti":
            if valuesAfter[i3] == i1:
                print "seti"
                count += 1
        elif opcode == "gtir":
            if (valuesAfter[i3] == 1 and i1 > valuesBefore[i2]) or (valuesAfter[i3] == 0 and i1 < valuesBefore[i2]):
                print "gtir"
                count += 1
        elif opcode == "gtri":
            if (valuesAfter[i3] == 0 and i2 > valuesBefore[i1]) or (valuesAfter[i3] == 1 and i2 < valuesBefore[i1]):
                print "gtri"
                count += 1
        elif opcode == "gtrr":
            if (valuesAfter[i3] == 1 and valuesBefore[i1] > valuesBefore[i2]) or (valuesAfter[i3] == 0 and valuesBefore[i1] < valuesBefore[i2]):
                print "gtrr"
                count += 1
        elif opcode == "eqir":
            if (valuesAfter[i3] == 1 and i1 == valuesBefore[i2]) or (valuesAfter[i3] == 0 and i1 != valuesBefore[i2]):
                print "eqir"
                count += 1
        elif opcode == "eqri":
            if (valuesAfter[i3] == 1 and i2 == valuesBefore[i1]) or (valuesAfter[i3] == 0 and i2 != valuesBefore[i1]):
                print "eqri"
                count += 1
        elif opcode == "eqrr":
            if (valuesAfter[i3] == 1 and valuesBefore[i1] == valuesBefore[i2]) or (valuesAfter[i3] == 0 and valuesBefore[i1] != valuesBefore[i2]):
                print "eqrr"
                count += 1
    return count

def solveInstructions(name):
    with open(name) as f:
        lineCounter = 0
        instGroup = []
        totalNum = 0
        totalCount = 0
        for line in f.readlines():
            if lineCounter < 3:
                if lineCounter == 1:
                    instGroup.append(map(int,list(line.rstrip().split(" "))))
                else:
                    instGroup.append(map(int,list(line.rstrip().split("[")[1].split("]")[0].replace(" ","").split(",")))) 
                lineCounter += 1
            elif lineCounter == 3:
                totalCount += 1
                if instructionCounter(instGroup[1], instGroup[0], instGroup[2]) >= 3:
                    totalNum += 1
                lineCounter = 0
                instGroup = []
                break

        print totalNum, totalCount
solveInstructions("input16.txt")
