from collections import defaultdict
twoOfAny = 0
threeOfAny = 0
with open("input2.txt") as f:
	for line in f.readlines():
		lineDict = defaultdict(lambda : 0)
		for letter in line:
			lineDict[letter] += 1
		if 2 in lineDict.values():
			twoOfAny += 1
		if 3 in lineDict.values():
			threeOfAny += 1
	
	print twoOfAny * threeOfAny
