file = open("input02")
total = 0
l = []
for line in file:
    line = line.strip()
    if line == '':
        l.append(total)
        total = 0
        continue
    total += int(line)
l.sort(reverse=True)
print(l[0])
print(sum(l[:3]))
