lines = open(input()).readlines()

references = []
head = dict()
prev = None
curr = head

key = 811589153
n_mixes = 10

for i, line in enumerate(lines):
    number = int(line.strip())*key
    curr["prev"] = prev
    curr["curr"] = number
    curr["next"] = dict()
    references.append((curr, number))
    prev = curr
    curr = curr["next"]
prev["next"] = head
head["prev"] = prev

N = len(references)

for ref, num in references*n_mixes:
    # print(f"{num}: ", end="")
    # curr = head
    # while curr["curr"] != head["prev"]["curr"]:
    #     print(curr["curr"], end=", ")
    #     curr = curr["next"]
    # print(head["prev"]["curr"])
    # input()
    if abs(num) % (N-1) == 0:
        continue
    curr = head

    ref["prev"]["next"] = ref["next"]
    ref["next"]["prev"] = ref["prev"]

    curr = ref
    if num >= 0:
        move = "next"
    else:
        move = "prev"
    for _ in range(abs(num) % (N-1)):
        curr = curr[move]
    if num >= 0:
        next = curr["next"]
        curr["next"] = ref
        ref["prev"] = curr
        ref["next"] = next
        next["prev"] = ref
    else:
        prev = curr["prev"]
        curr["prev"] = ref
        ref["next"] = curr
        ref["prev"] = prev
        prev["next"] = ref

zero = head
while zero["curr"] != 0:
    zero = zero["next"]

final = [0]
curr = zero["next"]
while curr["curr"] != 0:
    final.append(curr["curr"])
    curr = curr["next"]

print(final)
print(final[1000 % N], final[2000 % N], final[3000 % N])
print(final[1000 % N] + final[2000 % N] + final[3000 % N])
