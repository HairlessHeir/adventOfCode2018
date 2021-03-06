def readFile(filename):
    fileData = []
    with open(filename) as f:
        for numData in filter(None,f.readlines())[0].split(" "):
            fileData.append(int(numData))
    return fileData

def makeTree(leftovers, level):
    totals = 0
    node = {}
    node["metadata"] = []
    childrenAmount = int(leftovers[0])
    metadataAmount = int(leftovers[1])
    leftovers = leftovers[2:]
    if childrenAmount == 0:
        node["metadata"] = leftovers[:metadataAmount]
        leftovers = leftovers[metadataAmount:]
    else:
        for i in range(childrenAmount):
            node[i],leftovers,total = makeTree(leftovers,level+1)
            totals += total

    if not node["metadata"]:
        node["metadata"] = leftovers[:metadataAmount]
        leftovers = leftovers[metadataAmount:]
        if childrenAmount != 0:
            newMetadataAmount = []
            for metaDataValue in node["metadata"]:
                if metaDataValue > childrenAmount:
                    newMetadataAmount.append(0)
                else:
                    newMetadataAmount.append(sum(node[metaDataValue-1]["metadata"]))
            node["metadata"] = newMetadataAmount

    totals = sum(node["metadata"])
    return (node,leftovers,totals)

tree = {}
listOfTree = readFile("input8.txt")
tree = makeTree(listOfTree,0)
print tree[2]
