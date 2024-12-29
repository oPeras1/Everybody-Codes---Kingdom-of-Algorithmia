p = 0

with open("../input.txt") as f:
    p = int(f.readline().strip())

n = 202400000
mod = 10
hp = 10

total = 1
thickness = 1
width = 1

heights = [1]

while total < n:
    thickness = ((thickness * p) % mod) + hp

    width += 2

    heights.insert(0, 0)
    heights.append(0)

    for i in range(len(heights)):
        heights[i] += thickness

    numblocks = sum(heights)

    temp = p * width
    
    for i in range(1, len(heights) - 1):
        removedblocks = (temp * heights[i]) % hp
        numblocks -= removedblocks

    total = numblocks

print(total - n)