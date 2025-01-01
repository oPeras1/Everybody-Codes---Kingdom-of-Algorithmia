grids = []

with open('../input.txt', 'r') as f:
    lines = f.readlines()

grids_per_row = len(lines[0].split())

grids_per_column = int((len(lines)+1) / 9)


grids = [[] for _ in range(grids_per_row*grids_per_column)]

li = 0
for line in lines:
    codes = line.split()
    
    if line == '\n':
        li += grids_per_row
        continue
    
    for i, code in enumerate(codes):
        grids[i+li].append(code)
            

count = 0

for grid in grids:

    visited = []

    grid_transpose = list(map(list, zip(*grid)))

    for linha in grid:
        for k in range(len(linha)):
            char = linha[k]

            if char == "*":
                continue

            if char != ".":
                continue

            common = set(linha) & set(grid_transpose[k])

            for c in common:
                if c != "." and c != "*" and c not in visited:
                    visited.append(c)
                    break


    for k in range(len(visited)):
        char = visited[k]

        count += (k+1) * (ord(char)-64)

print(count)