last = []
acc = [0]

with open("input.txt") as file:
    for i in range(25):
        last.append(int(file.readline().strip()))
        acc.append(last[-1] + acc[-1])
    for line in file:
        num = int(line.strip())
        valid = False
        for i, a in enumerate(last[-25:]):
            for j, b in enumerate(last[-25:]):
                if j <= i:
                    continue
                if a + b == num:
                    valid = True
                    break
            if valid:
                break
        if not valid:
            invalid = num
            print("Invalid numer is:", num)
        last.append(num)
        acc.append(last[-1] + acc[-1])

acc.pop(0)
acc_set = set(acc)
for j, num_f in enumerate(acc):
    num_i = num_f-invalid
    if num_i not in acc_set:
        continue
    i = acc.index(num_i) + 1
    if i == j:
        continue
    maxi = max(last[i:j+1])
    mini = min(last[i:j+1])
    print(maxi, mini)
    print(maxi+mini)
