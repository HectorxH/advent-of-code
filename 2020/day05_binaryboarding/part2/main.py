import re


def xorToN(N):
    if N % 4 == 0:
        return N
    elif N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N+1
    else:
        return 0


def xorRange(a, b):
    return xorToN(a-1) ^ xorToN(b)


maxi = -1
mini = float("inf")
xor_acomulado = 0
with open("input.txt") as file:
    for line in file:
        line = re.sub("B|R", "1", re.sub("F|L", "0", line.strip()))
        row = int(line[:-3], base=2)
        col = int(line[-3:], base=2)
        id_seat = row*8+col
        maxi = max(maxi, id_seat)
        mini = min(mini, id_seat)
        xor_acomulado ^= id_seat

print(xorRange(mini, maxi) ^ xor_acomulado)
