from collections import deque

lines = open(input()).readlines()

rev_op = {
    "+": "-",
    "-": "+",
    "*": "/",
    "/": "*",
    "=": "=",
}

operations = dict()
operators = dict()
dependencies = dict()
rev_dep = dict()
numbers = dict()
for line in lines:
    line = line.strip().replace(": ", "=")
    name, num = line.split("=")
    num = num.split(" ")
    if name == "root":
        num[1] == "="
    if name == "humn":
        num = [-1]
    if len(num) == 1:
        dependencies[name] = []
        op = f"{int(num[0])}"
    else:
        dependencies[name] = [num[0], num[-1]]
        rev_dep[num[0]] = name
        rev_dep[num[-1]] = name
        op = f"numbers['{num[0]}']{num[1]}numbers['{num[2]}']"
        operators[name] = rev_op[num[1]]
    operations[name] = op
human_branch = set()
curr = "humn"
prev = None
while curr != "root":
    human_branch.add(curr)
    prev = curr
    curr = rev_dep[curr]

root1, root2 = dependencies["root"]

humn_root = prev
non_humn_root = root1 if root1 != humn_root else root2


def solve_fwd(name):
    if len(dependencies[name]) == 0:
        numbers[name] = eval(operations[name])
        return
    solve_fwd(dependencies[name][0])
    solve_fwd(dependencies[name][1])
    numbers[name] = eval(operations[name])


def solve_bwd(name, number):
    # print(name, number)
    if name == "humn":
        return number
    dep1, dep2 = dependencies[name]
    human_dep = dep1 if dep1 in human_branch else dep2
    non_human_dep = dep1 if dep1 not in human_branch else dep2
    solve_fwd(non_human_dep)
    number_temp = numbers[non_human_dep]
    if dep2 in human_branch and operators[name] == "*":
        number = eval(f"{number_temp}/{number}")
    elif dep2 in human_branch and operators[name] == "+":
        number = eval(f"{number_temp}-{number}")
    else:
        number = eval(f"{number}{operators[name]}{number_temp}")
    return solve_bwd(human_dep, number)


solve_fwd(non_humn_root)
number = numbers[non_humn_root]
print(solve_bwd(humn_root, number))
