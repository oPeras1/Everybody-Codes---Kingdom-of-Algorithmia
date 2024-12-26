
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
    for i in range(0, len(lines[0]), 2):
        count += getPotions(lines[0],i)
        count += getPotions(lines[0],i+1)

        if monster(lines[0],i) and monster(lines[0],i+1):
            count += 2

print(count)