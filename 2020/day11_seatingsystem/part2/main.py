def valid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M


def count_occupied(i, j, layout):
    N = len(layout)
    M = len(layout[0])
    total = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            x, y = i+di, j+dj
            while valid(x, y, N, M) and layout[x][y] == '.':
                x += di
                y += dj
            if valid(x, y, N, M) and layout[x][y] == '#':
                total += 1
    return total


def step(layout):
    prev = [x.copy() for x in layout]
    N = len(layout)
    M = len(layout[0])
    changed = False
    for i in range(N):
        for j in range(M):
            if prev[i][j] == 'L' and count_occupied(i, j, prev) == 0:
                layout[i][j] = '#'
                changed = True
            elif prev[i][j] == '#' and count_occupied(i, j, prev) >= 5:
                layout[i][j] = 'L'
                changed = True
    return changed


with open("input.txt") as file:
    layout = [list(line.strip()) for line in file]

while step(layout):
    pass

count = sum([x.count("#") for x in layout])

print(count)
