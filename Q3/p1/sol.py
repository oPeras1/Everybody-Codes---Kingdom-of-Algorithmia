grid = []

with open("../input.txt", "r") as f:
    grid = f.read().strip().split("\n")

    grid = [list(row) for row in grid]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                grid[y][x] = "1"

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def surrounded(grid, y, x, char):

    
    for dir in dirs:

        inside = (y + dir[0] >= 0 and y + dir[0] < len(grid) and x + dir[1] >= 0 and x + dir[1] < len(grid[0]))

        if inside and grid[y + dir[0]][x + dir[1]] == ".":
            return True
        
    return False

num = 1

count = 0

while True:
    countnum = 0

    replace = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == str(num):
                countnum += 1
            
            if surrounded(grid, y, x, str(num)):
                replace.add((y, x))
            else:
                grid[y][x] = str(num + 1)
    
    for y, x in replace:
        grid[y][x] = "."

    num += 1

    count += countnum

    if countnum == 0:
        break


print(count)