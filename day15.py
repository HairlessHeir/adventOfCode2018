class Character:
     def __init__(self,characterType,enemyType,x,y):
        self.type = characterType
        self.x = x
        self.y = y
        self.HP = 200
        self.attackPower = 3
        self.enemy = enemyType

def readFile(name):
    rows = []
    with open(name) as f:
        for line in f.readlines():
            rows.append(line.rstrip())
    return rows
##
rows = readFile("input15_test.txt")
charList = []
for row in rows:
    for el in row:
        if el == "E":
            pass
        elif el == "G":
            pass