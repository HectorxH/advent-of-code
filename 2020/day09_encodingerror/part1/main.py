last = []

with open("input.txt") as file:
    for i in range(25):
        last.append(int(file.readline().strip()))
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
            print(num)
        last.append(num)
