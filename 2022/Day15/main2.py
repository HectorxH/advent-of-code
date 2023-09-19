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
            if r1[0]-1 <= r2[0] <= r1[1]+1:
                newRanges.append((r1[0], max(r1[1], r2[1])))
                changed = True
            else:
                newRanges.append(r2)
                newRanges.append(r1)
        if (len(ranges) % 2):
            newRanges.append(ranges[-1])
        ranges = sorted(newRanges)
    return ranges


def invertRanges(ranges, search):
    newRanges = []
    for r in ranges:
        if r[1] >= search[0]:
            newRanges.append((max(r[0], search[0]), r[1]))
    ranges = newRanges
    newRanges = []
    for r in ranges:
        if r[0] <= search[1]:
            newRanges.append((r[0], min(r[1], search[1])))
    ranges = newRanges
    if len(ranges) == 2:
        return (ranges[0][1]+1, ranges[1][0]-1)
    else:
        r = ranges[0]
        if r[0] > search[0]:
            return (search[0]+1, r[0]-1)
        elif r[1] < search[1]:
            return (r[1]+1, search[1]-1)
        else:
            return -1


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

search = int(input("Min search: ")), int(input("Max search: "))

for row, ranges in rowRanges.items():
    if search[0] <= row <= search[1]:
        ranges = mergeRenges(sorted(ranges))
        r = invertRanges(ranges, search)
        if r != -1:
            print(ranges)
            print(row, r)
            print(r[0]*4000000+row)
            break
