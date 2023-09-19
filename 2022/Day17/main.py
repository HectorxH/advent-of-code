from tqdm.auto import tqdm

line = open(input()).readline().strip()
direction = [-1 if c == "<" else +1 for c in line]


shapes = [
    [
        [1, 1, 1, 1],
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1],
    ],
]

# (y, x)
sizes = [(1, 4), (3, 3), (3, 3), (4, 1), (2, 2)]
WALL = [1, 0, 0, 0, 0, 0, 0, 0, 1]
board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
]

height = 0
virtual_height = 0
shape = 0


def startPosition():
    return [height+4+sizes[shape][0], 3]


def valid(shape, pos):
    lenY, lenX = sizes[shape]
    for dy in range(lenY):
        for dx in range(lenX):
            if board[pos[0]-dy][pos[1]+dx] == 1 and shapes[shape][-dy-1][dx] == 1:
                return False
    return True


def place(shape, pos):
    global height, virtual_height, board
    lenY, lenX = sizes[shape]
    for dy in range(lenY):
        for dx in range(lenX):
            board[pos[0]-dy][pos[1] +
                             dx] = max(board[pos[0]-dy][pos[1]+dx], shapes[shape][-dy-1][dx])
    diff_height = max(0, pos[0]-height)
    height += diff_height
    virtual_height += diff_height
    for _ in range(height+5+sizes[(shape+1) % len(sizes)][0]-len(board)):
        board.append(WALL.copy())


enc = {
    (0, 1): 0,
    (1, 0): 1,
    (1, 1): 2,
}


def encodeLines(line1, line2):
    lines = zip(line1[1:-1], line2[1:-1])
    encode = 0
    for i, symb in enumerate(lines):
        encode += 3**i*enc[symb]
    return encode


limit = 2022
limit = 1000000000000
rocks = 0
i = 0

DP = [[[None for _ in line] for _ in range(3**7)] for _ in shapes]
print("Memory allocated")

pos = startPosition()
with tqdm(total=limit) as pbar:
    while rocks < limit:
        pos[0] -= 1
        if not valid(shape, pos):
            pos[0] += 1
            place(shape, pos)
            rocks += 1
            pbar.update(1)
            if all([board[pos[0]][i] | board[pos[0]+1][i] for i in range(9)]):
                bitset = encodeLines(board[pos[0]], board[pos[0]+1])
                if DP[shape][bitset][i] == None:
                    DP[shape][bitset][i] = []
                elif len(DP[shape][bitset][i]) < 2:
                    DP[shape][bitset][i].append((height, rocks))
                else:
                    dp = DP[shape][bitset][i]
                    dheight = dp[1][0] - dp[0][0]
                    drocks = dp[1][1] - dp[0][1]
                    n_jumps = (limit-rocks)//drocks
                    rocks += n_jumps*drocks
                    virtual_height += n_jumps*dheight
                    pbar.update(n_jumps*drocks)
                    if n_jumps > 0:
                        print(
                            f"\nTime traveling: {n_jumps} jumps of {drocks} rocks")

            shape = (shape+1) % len(shapes)
            pos = startPosition()

            # temp = board[pos[0]][pos[1]]
            # board[pos[0]][pos[1]] = 2
            # for l in board[:prevpos[0]-1:-1]:
            #     print("".join(map(lambda x: "#" if x ==
            #                       1 else "." if x == 0 else "X", l)))
            # print("----")
            # board[pos[0]][pos[1]] = temp

            # input()

            continue

        pos[1] += direction[i]
        if not valid(shape, pos):
            pos[1] -= direction[i]
        i = (i+1) % len(direction)


print(virtual_height)
