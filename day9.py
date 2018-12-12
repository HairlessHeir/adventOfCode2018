from collections import defaultdict
def readFile(filename):
	playerAmount, topScore = 0,0
	with open(filename) as f:
		for line in f.readlines():
			playerAmount,topScore = line.split(" ")[0],line.split(" ")[6]
	return (int(playerAmount),int(topScore))


def playMarbleGame(playerAmount,topScore):
	playerScore = defaultdict(lambda:0)
	currentPlayer = 0
	currentMarbleIndex = 0
	nextMarbleIndex = 0
	gameList = []
	for i in range(topScore+1):
		if i==0:
			gameList.append(i)
			currentMarbleIndex = nextMarbleIndex
			nextMarbleIndex = (nextMarbleIndex+1)%(len(gameList)+1)
			currentPlayer = (currentPlayer+1)%playerAmount
		elif i == 1:
			gameList.insert(nextMarbleIndex,i)
			currentMarbleIndex = nextMarbleIndex
			currentPlayer = (currentPlayer+1)%playerAmount
		elif i == 2:
			gameList.insert(nextMarbleIndex,i)
			currentMarbleIndex = nextMarbleIndex
			nextMarbleIndex = (nextMarbleIndex+i)%(len(gameList)+1)
			currentPlayer = (currentPlayer+1)%playerAmount
		elif i % 23 == 0:
			playerScore[currentPlayer] += i
			currentMarbleIndex -= 7
			if currentMarbleIndex <0:
				currentMarbleIndex += len(gameList)
			scoreAddition = gameList.pop(currentMarbleIndex)
			playerScore[currentPlayer] += scoreAddition
			currentPlayer = (currentPlayer+1)%playerAmount
			nextMarbleIndex = currentMarbleIndex+2
		else:
			gameList.insert(nextMarbleIndex,i)
			currentMarbleIndex = nextMarbleIndex
			nextMarbleIndex = (nextMarbleIndex+2)
			if nextMarbleIndex < len(gameList):
				pass
			elif nextMarbleIndex == len(gameList):
				pass
			else:
				nextMarbleIndex %= len(gameList)
			currentPlayer = (currentPlayer+1)%playerAmount
		#print gameList
		#print "C:",gameList[currentMarbleIndex]," @ ",currentMarbleIndex

	print max(playerScore.values())

playerAmount,topScore = readFile("input9.txt")
playMarbleGame(playerAmount,topScore)
'''playMarbleGame(10,1618)
playMarbleGame(13,7999)
playMarbleGame(17,1104)
playMarbleGame(21,6111)
playMarbleGame(30,5807)'''
