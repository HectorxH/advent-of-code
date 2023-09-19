count = 0
with open("input.txt") as file:
    for line in file:
        policy, password = map(lambda x: x.strip(), line.split(":"))
        interval, char = policy.split(" ")
        mini, maxi = map(int, interval.split("-"))
        if mini <= password.count(char) <= maxi:
            count += 1
print(count)
