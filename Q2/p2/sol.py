with open("../input.txt") as f:
    lines = f.readlines()
    lines[0] = lines[0][6:].strip()

    words = lines[0].split(",")
    
    count = 0

    for line in lines[2:]:
        line = line.strip()

        visited = set()

        
        for word in words:
            can = True
            addtovisit = set()
            for kc in range(len(line)):
                for _ in range(2):
                    if line[kc:].startswith(word):
                        for kw in range(len(word)):
                            if line[kc+kw] == word[kw]:
                                addtovisit.add(kc+kw)
                            else:
                                can = False
                                break
                    word = word[::-1]

            if can:
                visited = visited.union(addtovisit)

        count += len(visited)

    print(count)


