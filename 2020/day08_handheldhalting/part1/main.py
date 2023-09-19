with open("input.txt") as file:
    code = list(map(lambda x: x.strip().split(" "), file.readlines()))

visited = set([0])
pc = 0
acc = 0
while True:
    op, amount = code[pc]
    print(op, amount)
    if op == "nop":
        pc += 1
    elif op == "acc":
        acc += int(amount)
        pc += 1
    elif op == "jmp":
        pc += int(amount)
    if pc in visited:
        break
    visited.add(pc)

print(pc, acc)
