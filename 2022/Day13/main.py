lines = open(input()).read().split("\n\n")


def check(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            return 1
        elif l == r:
            return 0
        else:
            return -1
    elif type(l) == int and type(r) == list:
        return check([l], r)
    elif type(l) == list and type(r) == int:
        return check(l, [r])

    for i in range(max(len(l), len(r))):
        if i >= len(l):
            return 1
        if i >= len(r):
            return -1

        c = check(l[i], r[i])
        if c != 0:
            return c

    return 0


total = 0
for i, line in enumerate(lines):
    l, r = list(map(lambda x: eval(x.strip()), line.strip().split("\n")))
    if check(l, r) == 1:
        print(i, ":", l, r)
        total += i + 1

print(total)
