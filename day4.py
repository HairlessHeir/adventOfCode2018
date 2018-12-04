import re
from collections import namedtuple
from collections import defaultdict

def readFile():
	lines = []
	with open("input4.txt") as f:
		lines = f.readlines()
	return lines

def parseTimestamp(timestamp):
	sleep = re.compile(".*asleep")
	awake = re.compile(".*up")
	ts = timestamp.split(" ")

	#type: A - awake, S - sleep, #xxx - ID
	guard = namedtuple("guard",["date","time","type","ID"])
	dateData, timeData, typeOfData, ID = "","","",""

	dateData = ts[0][1:]
	timeData = ts[1][:-1]
	if sleep.match(timestamp):
		typeOfData = "S"
	elif awake.match(timestamp):
		typeOfData = "A"
	else:
		typeOfData = "G"
		ID = ts[3][1:]

	return guard(dateData,timeData,typeOfData,ID)

def sortTimestamps(stamp):
	return stamp.date + " " + stamp.time


def getGuard(timestamps):
	sortedTimestamps = []
	for timestamp in timestamps:
		sortedTimestamps.append(parseTimestamp(timestamp))
	sortedTimestamps.sort(key=sortTimestamps)
	
	guards = defaultdict(lambda : defaultdict(lambda : 0))
	guardID = ""
	startTime = 0
	endTime = 0
	for sTimestamp in sortedTimestamps:
		if sTimestamp.type == "G":
			guardID = sTimestamp.ID
		elif sTimestamp.type == "S":
			startTime = int(sTimestamp.time.split(":")[1])
		elif sTimestamp.type == "A":
			endTime = int(sTimestamp.time.split(":")[1])
			for i in range(endTime-startTime):
				guards[guardID][startTime+i] += 1
		else:
			print "You shouldn't be here."

	highestSleepTime = 0
	sleepiestGuardMinute = 0
	sleepiestGuardID = ""
	for guardID in guards.keys():
		sleepiestMinute = 0
		sleepiestMinuteTime = 0
		totalSleepTime = 0
		for guardTime in guards[guardID].keys():
			if sleepiestMinuteTime < guards[guardID][guardTime]:
				sleepiestMinuteTime = guards[guardID][guardTime]
				sleepiestMinute = guardTime
			totalSleepTime += int(guards[guardID][guardTime])

		if highestSleepTime < totalSleepTime:
			highestSleepTime = totalSleepTime
			sleepiestGuardMinute = sleepiestMinute
			sleepiestGuardID = guardID

	print int(sleepiestGuardID) * sleepiestGuardMinute
	

########
getGuard(readFile())
