import numpy as np
from PIL import Image

lines = open(input()).readlines()

reg = [1]
for line in lines:
    instruction = line.strip().split(" ")
    if instruction[0] == "noop":
        reg += [reg[-1]]
    else:
        reg += [reg[-1], reg[-1]+int(instruction[1])]

positions = [20, 60, 100, 140, 180, 220]
print(sum([reg[pos-1]*pos for pos in positions]))

image = []
for cycle, pos in enumerate(reg):
    pixelPos = cycle % 40
    if pixelPos == 0:
        image.append([])
    if pos-1 <= pixelPos <= pos+1:
        image[-1].append("#")
    else:
        image[-1].append(".")
print("\n".join(list(map(lambda x: "".join(x), image))))

A = np.array([np.array([255 if c == "#" else 0
                        for c in line]) for line in image[:-1]])
print(A.shape)
Image.fromarray(A).resize((400, 60), Image.Resampling.BOX).show()
