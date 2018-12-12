from collections import defaultdict, deque
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
	fasterGameList = deque([0])
	for i in range(1,topScore+1):
		currentPlayer = (currentPlayer+1)%playerAmount
		if i%23==0:
			fasterGameList.rotate(7)
			score = fasterGameList.pop()
			fasterGameList.rotate(-1)
			playerScore[currentPlayer]+=(score + i)
		else:
			fasterGameList.rotate(-1)
			fasterGameList.append(i)


	print max(playerScore.values())

playerAmount,topScore = readFile("input9.txt")
playMarbleGame(playerAmount,topScore*100)

'''playMarbleGame(10,1618)
playMarbleGame(13,7999)
playMarbleGame(17,1104)
playMarbleGame(21,6111)
playMarbleGame(30,5807)'''
