x_pos = 0
count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line[x_pos] == '#':
            count += 1
        x_pos = (x_pos+3) % len(line)

print(count)
