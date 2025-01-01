grids = []

with open('../input.txt', 'r') as f:
    lines = f.readlines()

grids_per_row = len(lines[0].strip().split("**"))-2

grids_per_column = int((len(lines)) / 6)


grids = [[] for _ in range(grids_per_row*grids_per_column)]

li = 0
k = 0
for k in range(grids_per_column):

    linesg = lines[k*6:(k*6)+8]

    for line in linesg:
        codes = []

        for i in range(grids_per_row):
            codes.append(line[i*6:(i*6)+8])
        
        
        for i, code in enumerate(codes):
            grids[i+li].append(code)

    li += grids_per_row
            

count = 0

for grid in grids:

    visiteda = []

    for _ in range(1):
        visited = []

        grid_transpose = list(map(list, zip(*grid)))

        later = []

        unsolvable = False

        for p in range(len(grid)):
            linha = grid[p]
            for k in range(len(linha)):
                char = linha[k]

                if char == "*":
                    continue

                if char != ".":
                    continue

                common = set(linha) & set(grid_transpose[k])

                canadd = True

                common = [c for c in common if c != "." and c != "*" and c != "?"]

                if len(common) > 1:
                    unsolvable = True

                for c in common:
                    if c not in visited:
                        visited.append(c)
                        canadd = False
                        break
                
                if canadd:
                    visited.append((p, k))
                    later.append((p, k))

            if unsolvable:
                break

        if unsolvable:
            break

        changed = 0

        for p, k in later:
            linha = grid[p]
            char = linha[k]

            union = set(linha) | set(grid_transpose[k])

            union = [c for c in union if c != "." and c != "*" and c != "?"]

            union = [c for c in union if c not in visited]

            if len(union) != 1:
                unsolvable = True

            for c in union:
                # get index of (p,k) in visited
                index = visited.index((p, k))
                visited[index] = c
                changed += 1
                break
        
        if unsolvable:
            break

        if changed != len(later):
            continue
        
        if visited == []:
            continue

        if visiteda == []:
            visiteda = visited

        if visiteda != visited:
            unsolvable = True
            break

    if unsolvable:
        continue
    
    

    for k in range(len(visiteda)):
        char = visited[k]

        count += (k+1) * (ord(char)-64)

