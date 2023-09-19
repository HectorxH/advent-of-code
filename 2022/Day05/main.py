stack_info, instructions = list(map(
    lambda x: x.split("\n"),
    open(input("Filename: ")).read().split("\n\n")
))

nStacks = int(stack_info[-1][-2])

stacks = []
for i in range(nStacks):
    stacks.append([])
    for line in stack_info[-2::-1]:
        box = line[1+i*4]
        if box != " ":
            stacks[-1].append(box)

for instruction in instructions:
    amnt, frm, to = list(map(int, instruction.split(" ")[1::2]))
    # stacks[to-1] += stacks[frm-1][:-amnt-1:-1]
    stacks[to-1] += stacks[frm-1][-amnt:]
    stacks[frm-1] = stacks[frm-1][:-amnt]
print("".join(list(map(lambda x: x[-1], stacks))))
