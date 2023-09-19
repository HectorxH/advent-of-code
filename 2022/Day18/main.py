lines = open(input()).readlines()

droplets = []
for line in lines:
    droplet = tuple(map(int, line.strip().split(",")))
    droplets.append(droplet)

droplet_set = set(droplets)
area = 0
for droplet in droplets:
    x, y, z = droplet
    area += 6
    for d in [-1, 1]:
        if (x+d, y, z) in droplet_set:
            area -= 1
        if (x, y+d, z) in droplet_set:
            area -= 1
        if (x, y, z+d) in droplet_set:
            area -= 1
print(area)
