grid = []

with open("../input.txt") as f:
    for line in f:
        grid.append(list(line.strip())) 

grid_transpose = list(map(list, zip(*grid)))

visited = []

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
                linha[k] = c
                visited.append(c)
                break

print("".join(visited))