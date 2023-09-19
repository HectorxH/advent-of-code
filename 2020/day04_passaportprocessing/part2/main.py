import re

all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
all_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid(passaport):
    try:
        byr = int(passaport["byr"])
        iyr = int(passaport["iyr"])
        eyr = int(passaport["eyr"])
        hgt_value = int(passaport["hgt"][:-2])
        hgt_unit = passaport["hgt"][-2:]
        hcl = passaport["hcl"]
        ecl = passaport["ecl"]
        pid = passaport["pid"]

        if not 1920 <= byr <= 2002:
            return False
        if not 2010 <= iyr <= 2020:
            return False
        if not 2020 <= eyr <= 2030:
            return False
        if hgt_unit == "cm" and not 150 <= hgt_value <= 193:
            return False
        elif hgt_unit == "in" and not 59 <= hgt_value <= 76:
            return False
        if re.fullmatch(r"#[0-9a-f]{6}", hcl) == None:
            return False
        if not ecl in all_ecl:
            return False
        if re.fullmatch(r"\d{9}", pid) == None:
            return False
    except ValueError as e:
        return False

    return True


with open("input.txt") as file:
    passaports = file.read()

valid_passaports = 0
passaports = passaports.split("\n\n")
for passaport in passaports:
    passaport = re.split(r"\s", passaport.strip())
    passaport = map(lambda x: x.strip().split(":"), passaport)
    fields, values = zip(*passaport)
    passaport = dict(zip(fields, values))

    counts = [fields.count(field) for field in all_fields]
    if all(counts[:-1]) and sum(counts) == len(fields) and valid(passaport):
        valid_passaports += 1

print(valid_passaports, "/", len(passaports))
