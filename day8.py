def readFile(filename):
    fileData = []
    with open(filename) as f:
        for numData in filter(None,f.readlines())[0].split(" "):
            fileData.append(int(numData))
    return fileData

def makeTree(leftovers):
    node = {}
    childrenAmount = int(leftovers[0])
    metadataAmount = int(leftovers[1])
    for i in range(childrenAmount):
        node[i] = dict()
    node["metadata"] = leftovers[-metadataAmount:]

    leftovers = leftovers[2:-metadataAmount]
    print node, leftovers
    return node

tree = {}
tree = makeTree(readFile("input8_test.txt"))
