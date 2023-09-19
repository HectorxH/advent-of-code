import re

G = dict()
with open("input.txt") as file:
    for line in file:
        line = re.split(r",|contain", line.strip().strip("."))
        bag, *contents = list(map(lambda x: x.strip(), line))
        bag, _ = bag.rsplit(" ", 1)
        for content in contents:
            if content == "contain no other bags":
                continue
            amount, color = content.split(" ", 1)
            color, _ = color.rsplit(" ", 1)
            if color not in G:
                G[color] = []
            G[color].append(bag)
        if bag not in G:
            G[bag] = []

total = 0
visited = set()
q = G["shiny gold"]
while len(q) > 0:
    bag = q[0]
    q = q[1:]
    if bag not in visited:
        visited.add(bag)
        total += 1
        q = q + G[bag]

print(total)
