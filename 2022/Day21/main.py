from collections import deque

lines = open(input()).readlines()

operations = dict()
dependencies = dict()
numbers = dict()
for line in lines:
    line = line.strip().replace(": ", "=")
    name, num = line.split("=")
    num = num.split(" ")
    if len(num) == 1:
        dependencies[name] = []
        op = f"{int(num[0])}"
    else:
        dependencies[name] = [num[0], num[-1]]
        op = f"numbers['{num[0]}']{num[1]}numbers['{num[2]}']"
    operations[name] = op


def solve(name):
    if len(dependencies[name]) == 0:
        numbers[name] = eval(operations[name])
        return
    solve(dependencies[name][0])
    solve(dependencies[name][1])
    numbers[name] = eval(operations[name])


solve("root")
print(numbers["root"])
