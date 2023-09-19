T = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def getResultScore(a, b):
    if a == b:
        return 3
    if (
        (a == 1 and b == 3) or
        (a == 2 and b == 1) or
        (a == 3 and b == 2)
    ):
        return 6
    else:
        return 0


P = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2,
    },
    'Y': {
        'A': 1,
        'B': 2,
        'C': 3,
    },
    'Z': {
        'A': 2,
        'B': 3,
        'C': 1,
    }
}


def getPlay(result, opponent):
    if result == 'X':
        pass
    elif result == 'Y':
        pass
    elif result == 'Z':
        pass


file = open(input("Filename: "))
totalScore = 0
for line in file:
    oponent, me = line.strip().split()
    totalScore += getResultScore(P[me][oponent], T[oponent]) + P[me][oponent]

print(totalScore)
