n = int(input())
inp = [list(map(int, input().split(" "))) for _ in range(n)]
for a, b in inp:
    print(pow(a, b, 10**9+7))
