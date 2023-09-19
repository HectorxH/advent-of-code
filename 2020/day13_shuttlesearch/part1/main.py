with open("input.txt") as file:
    t0 = int(file.readline().strip())
    ids = file.readline().strip().split(",")

mini = float("inf")
mini_id = 0
for id_bus in ids:
    if id_bus == 'x':
        continue
    id_bus = int(id_bus)
    off = t0 % id_bus
    if mini > id_bus - off or off == 0:
        mini = id_bus - off
        mini_id = id_bus

print(mini, mini_id)
print(mini*mini_id)
