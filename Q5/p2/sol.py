grid = []

with open("../input.txt", "r") as f:
    for line in f:
        l = list(line.strip().split(" "))
        grid.append(l)

keep = 0
numberd: dict[str, int] = dict()
while True:
    keep += 1

    k = (keep-1)%len(grid[0])

    num = grid[0][k]

    for i in range(1, len(grid)):
        grid[i-1][k] = grid[i][k]

    grid[-1][k] = "0"

    k = k-len(grid[0])+1

    reallen = 0

    for _ in range(len(grid)):
        if grid[_][k] != "0":
            reallen += 1
        else:
            break

    div = (int(num)-1)//reallen
    rest = (int(num)-1)%reallen

    left = div % 2 == 0

    if len(grid) < reallen+2:
        grid.append(["0"]*len(grid[0]))

    if left:

        for i in range(reallen, rest-1, -1):
            grid[i][k] = grid[i-1][k]

        grid[rest][k] = num

    else:

        for i in range(reallen, reallen-rest-1, -1):
            grid[i][k] = grid[i-1][k]

        grid[reallen-rest][k] = num

    number = "".join(grid[0])
    
    if number in numberd:
        numberd[number] += 1
    else:
        numberd[number] = 1

    if numberd[number] == 2024:
        print(int(keep)*int(number))
        break


