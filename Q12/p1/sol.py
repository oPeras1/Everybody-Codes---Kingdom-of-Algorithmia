targets = []

letters = dict()

maxy = 0

with open("../input.txt") as f:
    lines = f.readlines()
    maxy = len(lines)-1
    for y in range(maxy+1):
        line = lines[y]
        for x in range(len(line)):
            char = line[x]
            if char == "T":
                targets.append((y,x))
            elif char != "." and char != "=" and char != "\n":
                letters[char] = (y,x)

count = 0


for target in targets:
    found = False
    for letter in letters:
        k = 1
        yL, xL = letters[letter]
        yT, xT = target
        xLO = xL
        while k < abs(xLO-xT):
            yL, xL = letters[letter]
            yL -= k
            xL += 2*k
            while yL <= maxy:
                yL += 1
                xL += 1
                if (yL,xL) == (yT,xT):
                    found = True
                    break
            if found:
                break
            k += 1
        
        if found:
            count += k*(ord(letter)-64)
            break
        
print(count)

            

