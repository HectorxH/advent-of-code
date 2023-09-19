lines = open(input()).readlines()

max_x = 0
max_y = 0
max_z = 0

droplets = []
for line in lines:
    droplet = tuple(map(lambda x: int(x)+1, line.strip().split(",")))
    droplets.append(droplet)
    max_x = max(max_x, droplet[0])
    max_y = max(max_y, droplet[1])
    max_z = max(max_z, droplet[2])

droplet_set = set(droplets)
surface_set = set()
visited = set()

q = [(0, 0, 0)]
while len(q) > 0:
    droplet = q[-1]
    q.pop()
    x, y, z = droplet
    if not 0 <= x <= max_x+1 or not 0 <= y <= max_y+1 or not 0 <= z <= max_z+1:
        continue
    if droplet in visited:
        continue
    if droplet in droplet_set:
        surface_set.add(droplet)
        continue
    visited.add(droplet)
    for d in [-1, 1]:
        q.append((x+d, y, z))
        q.append((x, y+d, z))
        q.append((x, y, z+d))


area = 0
for droplet in surface_set:
    x, y, z = droplet
    for d in [-1, 1]:
        if (x+d, y, z) in visited:
            area += 1
        if (x, y+d, z) in visited:
            area += 1
        if (x, y, z+d) in visited:
            area += 1

print(area)
