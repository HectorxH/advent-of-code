G, instructions = open(input()).read().split("\n\n")
G = G.split("\n")

instructions = instructions.replace("R", " R ").replace("L", " L ").split(" ")

walls = set()
paths = set()

N = len(G)
M = max(len(l) for l in G)
G = [l + " "*(M-len(l)) for l in G]

for y in range(N):
    for x in range(M):
        # print(x, y)
        if G[y][x] == ".":
            paths.add((x, y))
        elif G[y][x] == "#":
            walls.add((x, y))


WE = [None for _ in range(N)]
for y in range(N):
    for x in range(M):
        if G[y][x] in [".", "#"]:
            WE[y] = x
            break

EW = [None for _ in range(N)]
for y in range(N):
    for x in range(M-1, -1, -1):
        if G[y][x] in [".", "#"]:
            EW[y] = x
            break

NS = [None for _ in range(M)]
for x in range(M):
    for y in range(N):
        if G[y][x] in [".", "#"]:
            NS[x] = y
            break

SN = [None for _ in range(M)]
for x in range(M):
    for y in range(N-1, -1, -1):
        if G[y][x] in [".", "#"]:
            SN[x] = y
            break


directions = [">", "v", "<", "^"]
loop = [WE, NS, EW, SN]


def Loop(pos_x, pos_y, direction):
    if direction in [0, 2]:
        pos_x = loop[direction][pos_y]
    else:
        pos_y = loop[direction][pos_x]
    return pos_x, pos_y


mov_x = [1, 0, -1, 0]
mov_y = [0, 1, 0, -1]

valid = walls.union(paths)

pos_x = None
pos_y = None
for x in range(M):
    if G[0][x] == ".":
        pos_x = x
        pos_y = 0
        break

viz = [[c for c in l] for l in G]

direction = 0
for t, instruction in enumerate(instructions):
    if instruction == "R":
        direction = (direction+1) % 4
    elif instruction == "L":
        direction = (direction-1) % 4
    else:
        instruction = int(instruction)
        for i in range(instruction):
            tmp_x = pos_x
            tmp_y = pos_y
            tmp_x += mov_x[direction]
            tmp_y += mov_y[direction]
            if (tmp_x, tmp_y) not in valid:
                tmp_x, tmp_y = Loop(tmp_x, tmp_y, direction)
            if (tmp_x, tmp_y) in paths:
                pos_x = tmp_x
                pos_y = tmp_y
            viz[pos_y][pos_x] = directions[direction]

print(pos_x, pos_y)
print((pos_y+1)*1000+(pos_x+1)*4+direction)

for l in viz:
    print("".join(l))
