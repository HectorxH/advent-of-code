import re

with open("input.txt") as file:
    passaports = file.read()

all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

valid_passaports = 0
passaports = passaports.split("\n\n")
for passaport in passaports:
    passaport = re.split(r"\s", passaport.strip())
    passaport = map(lambda x: x.strip().split(":"), passaport)
    fields, values = zip(*passaport)

    counts = [fields.count(field) for field in all_fields]
    if all(counts[:-1]) and sum(counts) == len(fields):
        valid_passaports += 1

print(valid_passaports, "/", len(passaports))
