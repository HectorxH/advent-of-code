G, instructions = open(input()).read().split("\n\n")
G = G.split("\n")

instructions = instructions.replace("R", " R ").replace("L", " L ").split(" ")

H = len(G)
W = max(len(l) for l in G)

N = int(input())

G = [list(l) + [" "]*(W-len(l)) for l in G]

neighbors = {
    0: [(1, 0), (2, 1), (3, 0), (5, 0)],
    1: [(4, 2), (2, 2), (0, 2), (5, 3)],
    2: [(1, 3), (4, 1), (3, 1), (0, 3)],
    3: [(4, 0), (5, 1), (0, 0), (2, 0)],
    4: [(1, 2), (5, 2), (3, 2), (2, 3)],
    5: [(4, 3), (1, 1), (0, 1), (3, 3)]
}

face = 0
faces = [None for _ in range(6)]
for r in range(0, H, N):
    for c in range(0, W, N):
        if G[r][c] != " ":
            faces[face] = (r, c)
            face += 1

walls = set()
paths = set()
for face in range(6):
    for r in range(N):
        for c in range(N):
            if G[faces[face][0]+r][faces[face][1]+c] == ".":
                paths.add((face, r, c))
            elif G[faces[face][0]+r][faces[face][1]+c] == "#":
                walls.add((face, r, c))

directions = [">", "v", "<", "^"]


def Loop(face, r, c, direction):
    dir = direction
    nface, ndir = neighbors[face][dir]
    if dir == 0 and ndir == 0:
        c = 0
    elif dir == 0 and ndir == 1:
        c = N-r-1
        r = 0
    elif dir == 0 and ndir == 2:
        r = N-r-1
        c = 49
    elif dir == 0 and ndir == 3:
        c = r
        r = 49
    elif dir == 1 and ndir == 0:
        r = N-c-1
        c = 0
    elif dir == 1 and ndir == 1:
        r = 0
    elif dir == 1 and ndir == 2:
        r = c
        c = 49
    elif dir == 1 and ndir == 3:
        c = N-c-1
        r = 49
    elif dir == 2 and ndir == 0:
        r = N-r-1
        c = 0
    elif dir == 2 and ndir == 1:
        c = r
        r = 0
    elif dir == 2 and ndir == 2:
        c = 49
    elif dir == 2 and ndir == 3:
        c = N-r-1
        r = 49
    elif dir == 3 and ndir == 0:
        r = c
        c = 0
    elif dir == 3 and ndir == 1:
        c = N-c-1
        r = 0
    elif dir == 3 and ndir == 2:
        r = N-c-1
        c = 49
    elif dir == 3 and ndir == 3:
        r = 49
    return nface, r, c, ndir


mov_r = [0, 1, 0, -1]
mov_c = [1, 0, -1, 0]

valid = walls.union(paths)

viz = [[elem for elem in l] for l in G]

face = 0
r = 0
c = 0
direction = 0
for t, instruction in enumerate(instructions):
    if instruction == "R":
        direction = (direction+1) % 4
    elif instruction == "L":
        direction = (direction-1) % 4
    else:
        instruction = int(instruction)
        for _ in range(instruction):
            viz[faces[face][0]+r][faces[face][1]+c] = directions[direction]
            tmp_face = face
            tmp_r = r
            tmp_c = c
            tmp_dir = direction
            tmp_r += mov_r[direction]
            tmp_c += mov_c[direction]
            if not (0 <= tmp_r < N) or not (0 <= tmp_c < N):
                tmp_face, tmp_r, tmp_c, tmp_dir = Loop(face, r, c, direction)
            if (tmp_face, tmp_r, tmp_c) in paths:
                face = tmp_face
                r = tmp_r
                c = tmp_c
                direction = tmp_dir
viz[faces[face][0]+r][faces[face][1]+c] = directions[direction]

print(r, c)
print((faces[face][0]+r+1)*1000+(faces[face][1]+c+1)*4+direction)

for l in viz:
    print("".join(l))
