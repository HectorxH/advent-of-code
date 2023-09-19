lines = open(input()).readlines()


def contein(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def covers(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]


total_1 = 0
total_2 = 0
for line in lines:
    a, b = line.split(',')
    a = list(map(int, a.split('-')))
    b = list(map(int, b.split('-')))

    if contein(a, b) or contein(b, a):
        total_1 += 1
    if covers(a, b) or covers(b, a):
        total_2 += 1

print(total_1, total_2)
