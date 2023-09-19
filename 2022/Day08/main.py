from pprint import pprint

Graph = list(map(
    lambda x: list(map(int, x.strip())),
    open(input()).readlines())
)

visible = [[0 for i in line] for line in Graph]

N = len(Graph)
M = len(Graph[0])

# L2R
for i in range(N):
    prevMax = -1
    for j in range(M):
        if Graph[i][j] > prevMax:
            visible[i][j] = 1
            prevMax = Graph[i][j]

# R2L
for i in range(N):
    prevMax = -1
    for j in reversed(range(M)):
        if Graph[i][j] > prevMax:
            visible[i][j] = 1
            prevMax = Graph[i][j]

# T2B
for j in range(M):
    prevMax = -1
    for i in range(N):
        if Graph[i][j] > prevMax:
            visible[i][j] = 1
            prevMax = Graph[i][j]

# B2T
for j in range(M):
    prevMax = -1
    for i in reversed(range(N)):
        if Graph[i][j] > prevMax:
            visible[i][j] = 1
            prevMax = Graph[i][j]

print(sum(map(sum, visible)))
# pprint(visible)
