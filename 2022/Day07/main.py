from functools import reduce

lines = open(input()).readlines()

directory = {}

cwd = ["/"]
cwd_unido = ""
new = False
i = 0
while i < len(lines):
    line = lines[i].strip().split(" ")
    if line[0] == '$':
        if new:
            new = False
            for j in range(1, len(cwd)):
                if not "/".join(cwd[:-j]) in directory:
                    directory["/".join(cwd[:-j])] = []
                directory["/".join(cwd[:-j])] += directory[cwd_unido]
        if line[1] == "cd":
            if line[2] == "/":
                cwd = ["/"]
            elif line[2] == "..":
                cwd = cwd[:-1]
            else:
                cwd += [line[2]]
        else:  # ls
            cwd_unido = "/".join(cwd)
            new = False
    else:  # files de ls
        if not "/".join(cwd) in directory:
            new = True
            directory[cwd_unido] = []
        if line[0] == "dir":
            directory[cwd_unido].append((0, line[1]))
        else:
            directory[cwd_unido].append((int(line[0]), line[1]))
    i += 1
if new:
    new = False
    for j in range(1, len(cwd)):
        if not "/".join(cwd[:-j]) in directory:
            directory["/".join(cwd[:-j])] = []
        directory["/".join(cwd[:-j])] += directory[cwd_unido]


totals = {}
for k, v in directory.items():
    totals[k] = reduce(lambda a, b: a+b[0], v, 0)

total = 0
for k, v in totals.items():
    if v <= 100000:
        total += v

print(total)

free_space = 70000000 - totals["/"]
target = 30000000 - free_space
values = sorted(list(totals.values()))
for value in values:
    if value >= target:
        print(value)
        break
