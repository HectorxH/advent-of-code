from math import gcd
from collections import deque


def lcm(a, b):
    return abs(a*b)//gcd(a, b)


lines = open(input()).read().split("\n")

H = len(lines)
W = len(lines[0])
T = lcm(H-2, W-2)

base = [[lines[x][y] if lines[x][y] in [".", "#"]
         else "." for y in range(W)] for x in range(H)]

G = [[base[x].copy() for x in range(H)] for _ in range(T)]

for x in range(H):
    for y in range(W):
        if lines[x][y] == ">":
            for t in range(T):
                G[t][x][1+(y-1+t) % (W-2)] = "#"
        elif lines[x][y] == "<":
            for t in range(T):
                G[t][x][1+(y-1-t) % (W-2)] = "#"
        elif lines[x][y] == "v":
            for t in range(T):
                G[t][1+(x-1+t) % (H-2)][y] = "#"
        elif lines[x][y] == "^":
            for t in range(T):
                G[t][1+(x-1-t) % (H-2)][y] = "#"


def BFS(start, end):
    visited = set()
    q = deque([start])
    while len(q) > 0:
        t, x, y = q.popleft()
        if (t % T, x, y) in visited:
            continue
        visited.add((t % T, x, y))
        for dx in [1, 0, -1]:
            for dy in [1, 0, -1]:
                if abs(dx) + abs(dy) == 2 \
                        or not 0 <= x+dx < H \
                        or not 0 <= y+dy < W \
                        or G[(t+1) % T][x+dx][y+dy] == "#":
                    continue
                if (x+dx, y+dy) == end:
                    return t+1
                q.append((t+1, x+dx, y+dy))


a = BFS((0, 0, 1), (H-1, W-2))
print(f"{a} = {a}")
b = BFS((a, H-1, W-2), (0, 1))
print(f"{b} = {a} + {b-a}")
c = BFS((b, 0, 1), (H-1, W-2))
print(f"{c} = {a} + {b-a} + {c-b}")
