lines = open(input("Filename: ")).readlines()

pos = 0
for line in lines:  # Para test
    for i in range(len(line)-14):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            break
