def priority(c):
    o = ord(c)
    if ord('a') <= o <= ord('z'):
        return o - ord('a') + 1
    else:
        return o - ord('A') + 27


rucksacks = open(input("Input file: ")).read().split("\n")

total = 0
for group in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]):
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])
    inter = list(first.intersection(second).intersection(third))[0]
    total += priority(inter)

print(total)
