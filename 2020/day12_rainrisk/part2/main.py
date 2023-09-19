def rotR(z, ang):
    if ang == 90:
        return z*(-1j)
    elif ang == 180:
        return z*(-1)
    elif ang == 270:
        return z*(1j)


instructions = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        a, b = line[0], line[1:]
        instructions.append((a, int(b)))

pos = complex(0, 0)
waypoint = complex(10, 1)
for inst, t in instructions:
    if inst == 'F':
        pos += waypoint*t
    elif inst == 'R':
        waypoint = rotR(waypoint, t)
    elif inst == 'L':
        waypoint = rotR(waypoint, 360-t)
    elif inst == 'N':
        waypoint += complex(0, t)
    elif inst == 'S':
        waypoint += complex(0, -t)
    elif inst == 'E':
        waypoint += complex(t)
    elif inst == 'W':
        waypoint += complex(-t)

print(pos)
print(abs(pos.real)+abs(pos.imag))
