p = 0

with open("../input.txt") as f:
    p = int(f.readline().strip())

n = 20240000
mod = 1111

total = 1
old = 1
width = 1

while total < n:
    old = (old * p) % mod

    width += 2

    total += old * width

missing = total - n

print(missing*width)