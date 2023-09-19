import re
from pprint import pprint

G = dict()
with open("input.txt") as file:
    for line in file:
        line = re.split(r",|contain", line.strip().strip("."))
        bag, *contents = list(map(lambda x: x.strip(), line))
        bag, _ = bag.rsplit(" ", 1)
        for content in contents:
            if content == "no other bags":
                continue
            amount, color = content.split(" ", 1)
            color, _ = color.rsplit(" ", 1)
            if color not in G:
                G[color] = []
            if bag not in G:
                G[bag] = []
            G[bag].append((color, int(amount)))


total = 0
q = G["shiny gold"]
while len(q) > 0:
    bag, amount = q[0]
    q = q[1:]
    total += amount
    q = q + list(map(lambda x: [x[0], x[1]*amount], G[bag]))

print(total)
