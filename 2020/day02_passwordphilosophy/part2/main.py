def xor(expr1, expr2):
    return expr1 ^ expr2


count = 0
with open("input.txt") as file:
    for line in file:
        policy, password = map(lambda x: x.strip(), line.split(":"))
        interval, char = policy.split(" ")
        first, second = map(int, interval.split("-"))
        try:
            if xor(password[first-1] == char, password[second-1] == char):
                count += 1
        except:
            pass
print(count)
