from functools import reduce

monkeysInfo = open(input()).read().split("\n\n")
nMonkey = len(monkeysInfo)


def getOperation(operator, number):
    if number == "old":
        if operator == "*":
            return lambda x: x * x
        elif operator == "+":
            return lambda x: x + x
    else:
        number = int(number)
        if operator == "*":
            return lambda x: x * number
        elif operator == "+":
            return lambda x: x + number


monkeys = []
for monkeyInfo in monkeysInfo:
    monkey = {}
    monkeyInfo = list(map(
        lambda x: x.strip().split(" "),
        monkeyInfo.split("\n")
    ))
    monkey["items"] = list(map(lambda x: int(x.strip(",")), monkeyInfo[1][2:]))
    monkey["operation"] = getOperation(monkeyInfo[2][4], monkeyInfo[2][5])
    monkey["divisor"] = int(monkeyInfo[3][3])
    monkey[True] = int(monkeyInfo[4][-1])
    monkey[False] = int(monkeyInfo[5][-1])
    monkeys.append(monkey)

superDP = {}

divisors = [monkey["divisor"] for monkey in monkeys]
commonMultiple = reduce(lambda a, b: a*b, divisors, 1)

nInspections = [0 for _ in range(nMonkey)]
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey["items"]:
            nInspections[i] += 1
            item = monkey["operation"](item)
            next = item % monkey["divisor"] == 0
            nextMonkey = monkey[next]
            monkeys[nextMonkey]["items"].append(item % commonMultiple)
        monkeys[i]["items"] = []

nInspectionsSorted = sorted(nInspections)
print(nInspectionsSorted[-1]*nInspectionsSorted[-2])
