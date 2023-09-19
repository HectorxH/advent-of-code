def count_ways(L):
    cache = [-1 for _ in L]
    cache[0] = 1
    print(cache)
    return _count_ways(L, len(L)-1, cache)


def _count_ways(L, i, cache):
    if cache[i] != -1:
        return cache[i]

    ways = 0
    curr = L[i]
    for diff in range(1, 4):
        if L[i]-L[i-diff] > 3 or i-diff < 0:
            break
        print("i=", i-diff)
        ways += _count_ways(L, i-diff, cache)
        print(i, "ways", ways)

    cache[i] = ways
    return ways


with open("input.txt") as file:
    adapters = [0]+[int(line.strip()) for line in file]

print(adapters)
adapters.sort()

print(count_ways(adapters))
