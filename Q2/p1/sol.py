with open("../input.txt") as f:
    lines = f.readlines()
    lines[0] = lines[0][6:].strip()

    words = lines[0].split(",")
    
    count = 0
    
    for word in words:
        count += lines[2].count(word)

    print(count)


