with open("input.txt") as file:
    adapters = [0]+[int(line.strip()) for line in file]

print(adapters)
adapters.sort()

diffs = []
for i in range(len(adapters)-1):
    diffs.append(adapters[i+1]-adapters[i])

diffs.append(3)

print(diffs)

print(diffs.count(1)*diffs.count(3))
