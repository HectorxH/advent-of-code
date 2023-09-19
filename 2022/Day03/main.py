def priority(c):
    o = ord(c)
    if ord('a') <= o <= ord('z'):
        return o - ord('a') + 1
    else:
        return o - ord('A') + 27


rucksacks = open(input("Input file: ")).read().split("\n")

total = 0
for rucksack in rucksacks:
    first = set(rucksack[:len(rucksack)//2])
    second = set(rucksack[len(rucksack)//2:])
    inter = list(first.intersection(second))[0]
    total += priority(inter)

print(total)
