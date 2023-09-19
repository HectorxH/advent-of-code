import math


lines = open(input()).readlines()

head = [0, 0]
tail = [0, 0]

visited = set([tuple(tail)])


def move(head, tail, direction):
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    elif direction == "U":
        head[1] += 1
    else:
        head[1] -= 1

    diff_x, diff_y = head[0]-tail[0], head[1]-tail[1]

    if abs(diff_x) > 1:
        diff_x = diff_x//abs(diff_x)
        tail[0] += diff_x
        tail[1] += diff_y

    if abs(diff_y) > 1:
        diff_y = diff_y//abs(diff_y)
        tail[0] += diff_x
        tail[1] += diff_y

    visited.add(tuple(tail))

    return head, tail


for line in lines:
    direction, amount = line.strip().split(" ")
    amount = int(amount)

    for i in range(amount):
        head, tail = move(head, tail, direction)

print(len(visited))
