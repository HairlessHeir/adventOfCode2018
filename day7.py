from collections import defaultdict
import itertools

def readFile(filename):
	lines = []
	partGraph = defaultdict(list)
	with open(filename) as f:
		for line in f.readlines():
			lines.append((line.split(" ")[1],line.split(" ")[7]))
			partGraph[line.split(" ")[1]].append(line.split(" ")[7])
	return partGraph

def makeSteps(parent,childrenDict):
	node = {}
	if len(childrenDict[parent]) > 0:
		for child in childrenDict[parent]:
			node[child] = makeSteps(child,childrenDict)
	return node

def canReachStep(node, steps, traveledNodes, level):
	canReach = True
	for stepParent in steps.keys():
		if node in steps[stepParent].keys():
			if stepParent not in traveledNodes:
				canReach = False
				break
		else:	
			canReach = canReach and canReachStep(node, steps[stepParent], traveledNodes,level+1)
			if canReach == False:
				break
	return canReach

def treePartWithParent(parent,completeTree):
	myTree = {}
	if parent in completeTree.keys():
		myTree = completeTree[parent]
	else:
		for child in completeTree.keys():
			newTree = treePartWithParent(parent, completeTree[child])
			if newTree != {}:
				myTree = newTree
				break
	return myTree

def travelNodes(nodes):
	childrenSet = set()
	childrenDict = defaultdict(lambda : 0)
	childrenIterator = list(itertools.chain(nodes.values()))
	
	for children in childrenIterator:
		for child in children:
			childrenSet.add(child)
			childrenDict[child] += 1

	firsts = []
	for value in nodes.keys():
		if value not in childrenSet:
			firsts.append(value)
	stepList = {}
	firsts.sort()
	for stepNode in firsts:
		stepList[stepNode] = makeSteps(stepNode,nodes)
	current = firsts[0]
	stepQueue = []
	for stepNode in firsts:
		stepQueue.append(stepNode)
	traveledNodes = []
	traveledNodes.append(current)
	while True:
		while True:
			if canReachStep(stepQueue[0],stepList, traveledNodes,1):
				current = stepQueue.pop(0)
				if current not in traveledNodes:
					traveledNodes.append(current)
				break
			else:
				temp = stepQueue.pop(0)
				stepQueue.append(temp)

		for value in treePartWithParent(current,stepList):
			if value not in stepQueue:
				stepQueue.append(value)
		stepQueue.sort()
		if len(stepQueue) == 0:
			break

	stringNodes = ""
	for node in traveledNodes:
		stringNodes += node
	
	print stringNodes


travelNodes(readFile("input7.txt"))