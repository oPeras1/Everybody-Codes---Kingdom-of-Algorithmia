
count = 0

def monster(line,i):
    if line[i] == "A":
        return True
    if line[i] == "B":
        return True
    elif line[i] == "C":
        return True
    elif line[i] == "D":
        return True
    return False

def getPotions(line,i):
    if line[i] == "A":
        return 0
    elif line[i] == "B":
        return 1
    elif line[i] == "C":
        return 3
    elif line[i] == "D":
        return 5
    return 0

with open("../input.txt") as f:
    lines = f.readlines()
    for i in range(0, len(lines[0]), 3):
        count += getPotions(lines[0],i)
        count += getPotions(lines[0],i+1)
        count += getPotions(lines[0],i+2)

        mcount = 0
        for j in range(3):
            if monster(lines[0],i+j):
                mcount += 1

        if mcount == 3:
            count += 6
        elif mcount == 2:
            count += 2

print(count)