instructions = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        a, b = line[0], line[1:]
        instructions.append((a, int(b)))

rotR = dict()
rotR[(-1, 0)] = (0, 1)
rotR[(0, 1)] = (1, 0)
rotR[(1, 0)] = (0, -1)
rotR[(0, -1)] = (-1, 0)

rotL = dict()
rotL[(-1, 0)] = (0, -1)
rotL[(0, -1)] = (1, 0)
rotL[(1, 0)] = (0, 1)
rotL[(0, 1)] = (-1, 0)

pos = [0, 0]
direction = (1, 0)
for inst, t in instructions:
    if inst == 'F':
        pos[0] += direction[0]*t
        pos[1] += direction[1]*t
    elif inst == 'R':
        for _ in range(t//90):
            direction = rotR[direction]
    elif inst == 'L':
        for _ in range(t//90):
            direction = rotL[direction]
    elif inst == 'N':
        pos[1] += t
    elif inst == 'S':
        pos[1] -= t
    elif inst == 'E':
        pos[0] += t
    elif inst == 'W':
        pos[0] -= t

print(pos)
print(sum(map(abs, pos)))
