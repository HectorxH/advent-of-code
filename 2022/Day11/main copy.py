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

# divisors = [monkey["divisor"] for monkey in monkeys]


nInspections = [0 for _ in range(nMonkey)]
iter = 0
while iter < 10000:
    # print(superDP)
    # allItems = tuple([item for monkey in monkeys for item in monkey["items"]])
    # if allItems not in superDP:
    #     superDP[allItems] = (nInspections, iter)
    # else:
    #     prevNInspections, prevIter = superDP[allItems]
    #     diffNInspections = [nInspections[i]-prevNInspections[i]
    #                         for i in range(len(nInspections))]
    #     diffIter = iter-prevIter

    #     while iter+diffIter < 10000:
    #         nInspections = [nInspections[i]+diffNInspections[i]
    #                         for i in range(len(nInspections))]
    #         iter += diffIter

    for i, monkey in enumerate(monkeys):
        for item in monkey["items"]:
            nInspections[i] += 1
            item = monkey["operation"](item)
            next = item % monkey["divisor"] == 0
            nextMonkey = monkey[next]
            monkeys[nextMonkey]["items"].append(item % 100000009)
        monkeys[i]["items"] = []

    iter += 1

nInspectionsSorted = sorted(nInspections)

print(nInspectionsSorted[-1]*nInspectionsSorted[-2])
