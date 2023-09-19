with open("input.txt") as file:
    groups = file.read().split("\n\n")

groups = map(lambda x: x.splitlines(), groups)

total = 0
for group in groups:
    s = dict()
    for person in group:
        person = person.strip()
        for answer in person:
            if answer not in s:
                s[answer] = 0
            s[answer] += 1
            if s[answer] == len(group):
                total += 1

print(total)
