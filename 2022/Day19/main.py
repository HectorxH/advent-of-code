lines = open(input()).readlines()

blueprints = []
limits = []
for line in lines:
    costs = []
    limit = [24, 24, 24, 24]
    line = line.strip().split(" ")
    costs.append((int(line[6]), 0, 0, 0))
    costs.append((int(line[12]), 0, 0, 0))
    costs.append((int(line[18]), int(line[21]), 0, 0))
    costs.append((int(line[27]), 0, int(line[30]), 0))
    blueprints.append(costs)

    limit[0] = min(
        limit[0],
        max(int(line[12]), int(line[18]), int(line[27]))
    )
    limit[1] = min(
        limit[1],
        int(line[21])
    )
    limit[2] = min(
        limit[2],
        int(line[30])
    )
    limits.append(limit)

best = -1
DP = []


def solve(t, robots, resources, blueprint):
    global best, DP
    if robots in DP[t] and resources in DP[t][robots]:
        return DP[t][robots][resources]
    if t == 24:
        best = max(best, resources[3])
        return resources[3]
    if resources[3] + (robots[3]+(24-t))*(24-t) <= best:
        return 0

    max_geode = 0
    for robot in range(3, -1, -1):
        if robots[robot] >= limits[blueprint][robot]:
            continue
        res_after = tuple(
            r - c for r, c in zip(resources, blueprints[blueprint][robot]))
        if all(map(lambda x: x >= 0, res_after)):
            bots_after = tuple(robots[r]+1 if r == robot else robots[r]
                               for r in range(4))
            res_after = tuple(res + bot for res, bot in zip(res_after, robots))
            max_geode = max(
                max_geode,
                solve(t+1, bots_after, res_after, blueprint)
            )

    res_after = tuple(res + rob for res, rob in zip(resources, robots))
    max_geode = max(
        max_geode,
        solve(t+1, robots,  res_after, blueprint)
    )

    if robots not in DP[t]:
        DP[t][robots] = dict()
    DP[t][robots][resources] = max_geode
    return max_geode


scores = []
ans = 0
for i, blueprint in enumerate(blueprints):
    print(f"{i}/{len(blueprints)}")
    DP = [dict() for _ in range(25)]
    best = -1
    scores.append(solve(0, (1, 0, 0, 0), (0, 0, 0, 0), i))
    ans += (i+1)*scores[i]
print(f"{len(blueprints)}/{len(blueprints)}")

print(scores)
print(ans)
