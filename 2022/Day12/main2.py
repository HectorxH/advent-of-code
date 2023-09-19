import heapq

G = list(map(
    lambda x: list(x.strip()),
    open(input()).readlines()
))

end = (-1, -1)

queue = []

for i, line in enumerate(G):
    for j, char in enumerate(line):
        if char == "S" or char == "a":
            G[i][j] = ord("a")-ord("a")
            heapq.heappush(queue, (0, (i, j)))
        elif char == "E":
            end = (i, j)
            G[i][j] = ord("z")-ord("a")
        else:
            G[i][j] = ord(char) - ord("a")

print("\n".join(map(lambda x: "\t".join(map(str, x)), G)))
print(queue[0][1])
print(end)

visited = [[False for _ in line] for line in G]
distance = [[float("inf") for _ in line] for line in G]


while len(queue) > 0:
    dist, [x, y] = heapq.heappop(queue)
    if distance[x][y] <= dist:
        continue
    distance[x][y] = dist
    if x == end[0] and y == end[1]:
        print(dist)
        break
    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            if abs(dx)+abs(dy) != 1:
                continue
            if not (0 <= x+dx < len(G)):
                continue
            if not (0 <= y+dy < len(G[0])):
                continue
            if G[x+dx][y+dy] > G[x][y]+1:
                continue
            heapq.heappush(queue, (dist+1, (x+dx, y+dy)))
