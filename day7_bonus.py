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
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	bufferStepTime = 0#60
	stepTimes = {}
	for i,letter in enumerate(letters):
		stepTimes[letter] = bufferStepTime+i+1
	numOfWorkers = 2
	workers = []

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
	print "ste:",stepQueue
	traveledNodes = []
	while True:

		for work in workers:
			stepTimes[work] -= 1	
			print "WORK: ",work," - ",stepTimes[work]
			if stepTimes[work] <= 0:
				traveledNodes.append(work)
				break
		for work in traveledNodes:
			workers.remove(work)

		while True:
			#print "--: ",stepQueue,workers,traveledNodes,stepTimes
			if len(stepQueue) == 0:
				break
			if canReachStep(stepQueue[0],stepList, traveledNodes,1):
				if len(workers) >= numOfWorkers:
					break
				if stepQueue[0] not in workers and stepQueue[0] not in traveledNodes:
					current = stepQueue.pop(0)
					workers.append(current)
			else:
				temp = stepQueue.pop(0)
				stepQueue.append(temp)

		for worker in workers:
			for value in treePartWithParent(worker,stepList):
				if value not in stepQueue and value not in workers:
					stepQueue.append(value)
		stepQueue.sort()
		if len(stepQueue) == 0:
			break

	stringNodes = ""
	for node in traveledNodes:
		stringNodes += node
	
	print stringNodes


travelNodes(readFile("input7_test.txt"))