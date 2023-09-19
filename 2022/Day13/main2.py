from functools import cmp_to_key

lines = [eval(line.strip())
         for line in open(input()).readlines() if line.strip() != ""] + [[[2]], [[6]]]


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


lines.sort(key=cmp_to_key(check), reverse=True)
total = 1
for i, line in enumerate(lines):
    if line == [[2]] or line == [[6]]:
        total *= i+1
print(total)
exit()
