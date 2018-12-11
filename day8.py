def readFile(filename):
    fileData = []
    with open(filename) as f:
        for numData in filter(None,f.readlines())[0].split(" "):
            fileData.append(int(numData))
    return fileData

def makeTree(leftovers, level):
    #print "B_leftovers:",leftovers
    totals = 0
    node = {}
    node["metadata"] = []
    childrenAmount = int(leftovers[0])
    metadataAmount = int(leftovers[1])
    #print "   "*level,"Node:({0},{1})".format(childrenAmount,metadataAmount)
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

    totals += sum(node["metadata"])
    #print "   "*(level),"-data:",str(node["metadata"]),":",totals
    #print "A_leftovers:", leftovers
    return (node,leftovers,totals)

tree = {}
listOfTree = readFile("input8.txt")
#print listOfTree
tree = makeTree(listOfTree,0)
print tree[2]
