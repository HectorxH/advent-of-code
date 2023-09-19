from itertools import combinations
print(max(map(sum, combinations(map(lambda x: sum(map(int, x.split('\n'))),
                                    open("input02").read().split('\n\n')), 3))))
