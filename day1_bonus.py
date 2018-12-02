from sets import Set

with open("input1.txt") as f:
    frequency = 0
    freqs = Set([0])
    found = False
    while found != True:
        for calibration in f.readlines():
            frequency += int(calibration)
            if frequency not in freqs:
                freqs.add(frequency)
            else:
                found = True
                print frequency
                break
        f.seek(0)