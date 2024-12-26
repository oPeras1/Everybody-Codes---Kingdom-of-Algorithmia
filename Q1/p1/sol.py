
count = 0

with open("../input.txt") as f:
    lines = f.readlines()
    for char in lines[0]:
        if char == "B":
            count += 1
        elif char == "C":
            count += 3

print(count)