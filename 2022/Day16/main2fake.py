lines = open(input()).readlines()

V = 0
node_to_int = dict()
int_to_node = []

G_flow = []
G_neighbors = []

non_zero = []

for line in lines:
    line = line.replace("=", " ").replace(
        ";", "").replace(",", "").strip().split(" ")
    node = line[1]
    int_to_node.append(node)
    node_to_int[node] = V
    G_flow.append(int(line[5]))
    G_neighbors.append(line[10:])
    if G_flow[V] > 0:
        non_zero.append(V)
    V += 1

dist = [[float("inf") for _ in range(V)] for _ in range(V)]
for node, neighbors in enumerate(G_neighbors):
    for neighbor in neighbors:
        dist[node][node_to_int[neighbor]] = 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


visited = [False for _ in range(V)]

time1 = 26
time2 = 26
preassure = 0
max_preassure = 0


def solve(node1, node2):
    global time1, time2, preassure, max_preassure, visited
    if time1 <= 0 or time2 <= 0:
        return
    max_preassure = max(max_preassure, preassure)
    for neighbor1 in non_zero:
        if visited[neighbor1]:
            continue
        time1 -= (dist[node1][neighbor1]+1)
        preassure += time1*G_flow[neighbor1]
        visited[neighbor1] = True
        for neighbor2 in non_zero:
            if node1 == 0 and node2 == 0:
                print(neighbor1, neighbor2)
            if visited[neighbor2]:
                continue
            time2 -= (dist[node2][neighbor2]+1)
            preassure += time2*G_flow[neighbor2]
            visited[neighbor2] = True
            solve(neighbor1, neighbor2)
            visited[neighbor2] = False
            preassure -= time2*G_flow[neighbor2]
            time2 += (dist[node2][neighbor2]+1)
        visited[neighbor1] = False
        preassure -= time1*G_flow[neighbor1]
        time1 += (dist[node1][neighbor1]+1)


solve(0, 0)
print(max_preassure)
# DP = [[dict() for _ in range(V)] for _ in range(31)]
# DP[0][0][0] = 0

# ans = 0
# for time in range(31):
#     print(f"\r{time}/30, {sum(map(len, DP[time]))}", end="")
#     for node in [0] + non_zero:
#         for visited, released in DP[time][node].items():
#             visited = visited | (1 << node)
#             for neighbor in non_zero:
#                 arrival_time = time+dist[node][neighbor]+1
#                 if (visited & (1 << neighbor)) > 0 or arrival_time > 30:
#                     continue
#                 new_released = released+(30-arrival_time)*G_flow[neighbor]
#                 if visited not in DP[arrival_time][neighbor]:
#                     DP[arrival_time][neighbor][visited] = new_released
#                 elif DP[arrival_time][neighbor][visited] < new_released:
#                     ans = max(ans, new_released)
#                     DP[arrival_time][neighbor][visited] = new_released

# print()
# print(ans)

# total = 0
# time = 0
# visited = [False for _ in range(V)]
# prev = 0

# while time <= 30:
#     best_score = float("-inf")
#     best_node = -1
#     for node in range(1, V):
#         if visited[node]:
#             continue
#         new_time = time+dist[prev][node]+1
#         score = (30-new_time)*G_flow[node]
#         if score > best_score:
#             best_score = score
#             best_node = node
#     time = time+dist[prev][best_node]+1
#     total += (30-time)*G_flow[best_node]
#     visited[best_node] = True
#     prev = best_node
#     print(int_to_node[prev])


# print(total)
