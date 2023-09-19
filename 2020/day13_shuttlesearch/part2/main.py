with open("input.txt") as file:
    _ = int(file.readline().strip())
    ids = file.readline().strip().split(",")

prod = 1
for id_bus in ids:
    if id_bus != 'x':
        prod *= int(id_bus)

p = []
for id_bus in ids:
    if id_bus == 'x':
        p.append('x')
    else:
        p.append(prod//int(id_bus))

inv = []
for i, id_bus in enumerate(ids):
    if id_bus == 'x':
        inv.append('x')
    else:
        inv.append(pow(p[i], -1, int(id_bus)))

print(ids)
print(p)
print(inv)

ans = 0
for i in range(len(ids)):
    if ids[i] == 'x':
        continue
    ans += -(i % int(ids[i]))*p[i]*inv[i]

print(ans)
print(ans % prod)
