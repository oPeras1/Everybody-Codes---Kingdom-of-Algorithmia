n = 0

with open("../input.txt") as f:
    n = int(f.readline().strip())

total = 1
old = 1

while total < n:
    old += 2
    total += old

missing = total - n

print(missing*old)