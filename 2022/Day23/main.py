lines = open(input()).readlines()

directions = [
    ((-1,  0), (-1, -1), (-1,  1)),  # N
    ((1,  0), (1, -1), (1,  1)),  # S
    ((0, -1), (-1, -1), (1, -1)),  # W
    ((0,  1), (-1,  1), (1,  1)),  # E
]


def posAdd(pos, dpos):
    return (pos[0]+dpos[0], pos[1]+dpos[1])


id = 0
poss = set()
elfs = []
for x, line in enumerate(lines):
    line = line.strip()
    for y, c in enumerate(line):
        if c == "#":
            elfs.append((x, y))
            poss.add((x, y))
            id += 1

offset = 0
while True:
    moves = dict()
    for elf_id in range(id):
        x, y = elfs[elf_id]
        alone = True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if (x+dx, y+dy) in poss:
                    alone = False
        if alone:
            continue
        for direction in range(4):
            main, left, right = directions[(direction+offset) % 4]
            main = posAdd((x, y), main)
            left = posAdd((x, y), left)
            right = posAdd((x, y), right)
            if main in poss or left in poss or right in poss:
                continue
            if main in moves:
                del moves[main]
            else:
                moves[main] = elf_id
            # print(f"{offset}: Elf {elf_id} wants to move to {(x, y)}")
            break
    if len(moves) == 0:
        break
    for move, elf_id in moves.items():
        poss.remove(elfs[elf_id])
        elfs[elf_id] = move
        poss.add(move)
    offset += 1

min_x = float("inf")
min_y = float("inf")
max_x = float("-inf")
max_y = float("-inf")
for x, y in elfs:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

H = max_x - min_x + 1
W = max_y - min_y + 1

print(H*W-id)
print(offset+1)
