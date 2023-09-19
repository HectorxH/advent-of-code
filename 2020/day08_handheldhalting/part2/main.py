def check(code, visited):
    N = len(code)
    pc = 0
    acc = 0
    while pc < N:
        op, amount = code[pc]
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += int(amount)
            pc += 1
        elif op == "jmp":
            pc += int(amount)
        if pc in visited:
            return False, acc
        visited.add(pc)
    return True, acc


with open("input.txt") as file:
    code = list(map(lambda x: x.strip().split(" "), file.readlines()))

visited = set([0])
check(code, visited)

for pc in visited:
    op, amount = code[pc]
    if op == "nop":
        code[pc] = ["jmp", amount]
    elif op == "jmp":
        code[pc] = ["nop", amount]

    flag, acc = check(code, set([0]))
    if flag:
        print(acc)
    code[pc] = op, amount
