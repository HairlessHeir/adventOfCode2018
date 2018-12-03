from collections import defaultdict
import sys

with open("input2.txt") as f:
	lines = f.readlines()
	for i, boxA_ID in enumerate(lines,start=0):
		for j, boxB_ID in enumerate(lines[i:],start=i):
			if i != j:
				differentLetters = 0
				sameLetters = []
				for letterA,letterB in zip(boxA_ID,boxB_ID):
					if letterA != letterB:
						differentLetters += 1
					else:
						sameLetters.append(letterA)
				if differentLetters == 1:
					for letter in sameLetters:
						sys.stdout.write(letter)
					break
	
