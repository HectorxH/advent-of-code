import re

maxi = -1
with open("input.txt") as file:
    for line in file:
        line = re.sub("B|R", "1", re.sub("F|L", "0", line.strip()))
        row = int(line[:-3], base=2)
        col = int(line[-3:], base=2)
        maxi = max(maxi, row*8+col)

print(maxi)
