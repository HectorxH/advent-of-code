lines = open(input()).readlines()

N = 10
segments = [[0, 0] for _ in range(N)]
visited = set([tuple([0, 0])])

for line in lines:
    direction, amount = line.strip().split(" ")
    amount = int(amount)
    for i in range(amount):
        if direction == "R":
            segments[0][0] += 1
        elif direction == "L":
            segments[0][0] -= 1
        elif direction == "U":
            segments[0][1] += 1
        elif direction == "D":
            segments[0][1] -= 1

        for i in range(1, N):
            head = segments[i-1]
            tail = segments[i]
            diff_x, diff_y = head[0]-tail[0], head[1]-tail[1]

            if abs(diff_x) > 1:
                diff_x = diff_x//abs(diff_x)
            if abs(diff_y) > 1:
                diff_y = diff_y//abs(diff_y)
            if abs(diff_x) > 1 or abs(diff_y) > 1:
                tail[0] += diff_x
                tail[1] += diff_y

            segments[i] = tail
        visited.add(tuple(segments[-1]))

print(len(visited))
