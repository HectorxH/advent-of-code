lines = open(input()).readlines()

minX = 100000
maxX = 0
maxY = 0

paths = []
for line in lines:
    points = line.strip().split(" -> ")
    paths.append([])
    for point in points:
        x, y = list(map(int, point.split(",")))
        minX = min(minX, x)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        paths[-1].append((x, y))

for i, path in enumerate(paths):
    for j, (x, y) in enumerate(path):
        paths[i][j] = (x-minX, y)

lenX = maxX-minX
G = [[0 for _ in range(maxY+1)] for _ in range(lenX+1)]


def printG():
    GT = list(zip(*G))
    for line in GT:
        print("".join(map(str, line)))
    print("-"*lenX)


for path in paths:
    x, y = path[0]
    for nextX, nextY in path:
        while x != nextX or y != nextY:
            G[x][y] = 1
            if x > nextX:
                x -= 1
            elif x < nextX:
                x += 1
            elif y > nextY:
                y -= 1
            elif y < nextY:
                y += 1
    G[x][y] = 1

totalSand = 0


def dropSand(x, y):
    global G, totalSand
    if y+1 > maxY:
        return False
    if G[x][y+1] == 0:
        return dropSand(x, y+1)
    if x-1 < 0:
        return False
    if G[x-1][y+1] == 0:
        return dropSand(x-1, y+1)
    if x+1 > lenX:
        return False
    if G[x+1][y+1] == 0:
        return dropSand(x+1, y+1)
    # print(x, y)
    G[x][y] = 2
    totalSand += 1
    return True


while dropSand(500-minX, 0):
    # printG()
    pass

printG()
print(totalSand)
