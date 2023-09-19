with open("input.txt") as file:
    groups = file.read().split("\n\n")

groups = map(lambda x: x.splitlines(), groups)

total = 0
for group in groups:
    s = set()
    for person in group:
        person = person.strip()
        for answer in person:
            s.add(answer)
    total += len(s)

print(total)
