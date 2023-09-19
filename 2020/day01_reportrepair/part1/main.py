numbers = set()
with open("input.txt") as file:
    for line in file:
        x = int(line)
        if (2020-x) in numbers:
            print(x*(2020-x))
        numbers.add(x)
