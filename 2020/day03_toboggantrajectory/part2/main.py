def checkCollisions(r, d, G):
    N = len(G[0])
    M = len(G)
    x_pos = 0
    y_pos = 0
    count = 0
    while True:
        if G[y_pos][x_pos]:
            count += 1
        x_pos = (x_pos+r) % N
        y_pos = y_pos+d
        if y_pos >= M:
            return count


G = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        G.append([char == '#' for char in line])

total = checkCollisions(1, 1, G)
total *= checkCollisions(3, 1, G)
total *= checkCollisions(5, 1, G)
total *= checkCollisions(7, 1, G)
total *= checkCollisions(1, 2, G)

print(total)
