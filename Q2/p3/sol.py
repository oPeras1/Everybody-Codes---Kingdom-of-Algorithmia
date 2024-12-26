with open("../input.txt", "r") as f:
    text = f.read().strip()
    lines = text.split("\n")  

runes = lines[0].split(":")[1].split(",")
grid = lines[2:]

width = len(grid[0])
height = len(grid)

addtovisit = set()

for rune in runes:
    rune_len = len(rune)

    for row, line in enumerate(grid):
        line_len = len(line)

        if rune_len > line_len:
            continue

        for i in range(0, line_len):
            section = ""

            if i + rune_len < line_len:
                section = line[i:i+rune_len]
            else:
                section = line[i:] + line[:i+rune_len-line_len]

            if section == rune or section == rune[::-1]:

                for j in range(i, i+rune_len):
                    if j >= line_len:
                        addtovisit.add((row, j-line_len))
                    else:
                        addtovisit.add((row, j))

    for col in range(width):
        if rune_len > height:
            continue

        for i in range(0, height - rune_len + 1):
            section = ""

            for w in range(0, rune_len):
                section += grid[i+w][col]

            if section == rune or section == rune[::-1]:
                for j in range(i, i+rune_len):
                    if j >= height:
                        addtovisit.add((j-height, col))
                    else:
                        addtovisit.add((j, col))

print(len(addtovisit))