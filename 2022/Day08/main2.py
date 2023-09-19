Graph = list(map(
    lambda x: list(map(int, x.strip())),
    open(input()).readlines())
)

maxScore = 0
N = len(Graph)
M = len(Graph[0])

for i, line in enumerate(Graph):
    for j, hight in enumerate(line):
        dists = [0, 0, 0, 0]
        for x in range(1, i+1):
            if Graph[i-x][j] >= hight:
                dists[0] += 1
                break
            dists[0] += 1
        for x in range(1, N-i):
            if Graph[i+x][j] >= hight:
                dists[1] += 1
                break
            dists[1] += 1
        for y in range(1, j+1):
            if Graph[i][j-y] >= hight:
                dists[2] += 1
                break
            dists[2] += 1
        for y in range(1, M-j):
            if Graph[i][j+y] >= hight:
                dists[3] += 1
                break
            dists[3] += 1
        # print(hight, dists)
        maxScore = max(maxScore, dists[0]*dists[1]*dists[2]*dists[3])

print(maxScore)
