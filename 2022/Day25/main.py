from functools import reduce

lines = open(input()).readlines()

digits = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

r_digits = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
}

s_to_result = {
    -5: ("0", "-"),
    -4: ("1", "-"),
    -3: ("2", "-"),
    -2: ("=", "0"),
    -1: ("-", "0"),
    0: ("0", "0"),
    1: ("1", "0"),
    2: ("2", "0"),
    3: ("=", "1"),
    4: ("-", "1"),
    5: ("0", "1"),
}


def toInt(a):
    return int("".join([c if c in "12" else "0" for c in a]), 5) - int("".join(["1" if c == "-" else "2" if c == "=" else "0" for c in a]), 5)


def rAdd(a, b, c="0"):
    s = digits[a] + digits[b] + digits[c]
    return s_to_result[s]


def add(a, b):
    max_len = max(len(a), len(b))
    a = "0"*(max_len-len(a))+a
    b = "0"*(max_len-len(b))+b
    s = ""
    r = "0"
    for i in range(-1, -max_len-1, -1):
        t, r = rAdd(a[i], b[i], r)
        s = t + s
    return s


s = lines[0].strip()
for line in lines[1:]:
    line = line.strip()
    s = add(s, line)
print(s)
