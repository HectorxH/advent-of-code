lines = open(input()).readlines()


def mDist(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])


def mergeRenges(ranges):
    changed = True
    while changed:
        changed = False
        newRanges = []
        for i in range(0, len(ranges)-1, 2):
            r1 = ranges[i]
            r2 = ranges[i+1]
            if r1[0] <= r2[0] <= r1[1]:
                newRanges.append((r1[0], max(r1[1], r2[1])))
                changed = True
            else:
                newRanges.append(r2)
                newRanges.append(r1)
        if (len(ranges) % 2):
            newRanges.append(ranges[-1])
        ranges = sorted(newRanges)
    return ranges


sensors = []
beacons = []
for line in lines:
    line = list(map(
        lambda x: x.strip().split(" "),
        line.strip().split(", ")
    ))
    xS = int(line[0][-1][2:])
    yS = int(line[1][0][2:-1])
    xB = int(line[1][-1][2:])
    yB = int(line[2][0][2:])
    sensors.append((xS, yS))
    beacons.append((xB, yB))

rowRanges = dict()
for sensor, beacon in zip(sensors, beacons):
    dist = mDist(sensor, beacon)
    for dy in range(-dist, dist+1):
        rDist = dist-abs(dy)
        currY = sensor[1]+dy
        if currY not in rowRanges:
            rowRanges[currY] = []
        rowRanges[currY].append((sensor[0]-rDist, sensor[0]+rDist))

target = int(input("Row: "))
ranges = sorted(rowRanges[target])

ranges = mergeRenges(ranges)
counts = [r[1]-r[0] for r in ranges]

print(sum(counts))
