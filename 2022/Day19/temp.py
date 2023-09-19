lines = open(input()).readlines()


def encodeHistorial(historial):
    encode = 0
    exp = 1
    for num in historial:
        encode += num*exp
        exp *= 5
    return encode


def decodeHistorial(encode):
    decode = []
    exp = 5**23
    for _ in range(24):
        num = encode//exp
        decode.append(num)
        encode -= num*exp
        exp //= 5
    decode.reverse()
    return decode


a = [1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 3, 3, 3, 0, 0, 0, 4, 4, 4, 0, 0, 0]
print(a)
print(encodeHistorial(a))
print(decodeHistorial(encodeHistorial(a)))


DP = [dict()]*24
DP[0][0] =


def solve(t, historial):
    enc = encodeHistorial(historial)
    if enc in DP:
        return DP[enc]


blueprints = []
for line in lines:
    costs = []
    line = line.strip().split(" ")
    costs.append((int(line[6]), 0, 0, 0))
    costs.append((int(line[12]), 0, 0, 0))
    costs.append((int(line[18]), int(line[21]), 0, 0))
    costs.append((int(line[27]), 0, int(line[30]), 0))
    blueprints.append(costs)
