numbers = set()
with open("input.txt") as file:
    for line in file:
        x = int(line)
        for y in numbers:
            if (2020-x-y) in numbers:
                print(x*y*(2020-x-y))
        numbers.add(x)
