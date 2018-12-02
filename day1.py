with open("input1.txt") as f:
	frequency = 0
	for line in f.readlines():
		frequency += int(line)
	print frequency	