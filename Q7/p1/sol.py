calculations = {}

with open("../input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        
        letter = line[0]

        signal = line[2:].split(",")

        calculations[letter] = signal

def getsum(letter, k):
    signal = calculations[letter][k]

    if signal == "+":
        return 1
    elif signal == "-":
        return -1
    elif signal == "=":
        return 0

sums = {}
default = 10

for letter in calculations:
    num = default
    sum = 0

    for k in range(10):
        k = (k)%len(calculations[letter])

        num += getsum(letter, k)

        sum += num

    sums[letter] = sum

#sort by max value to min value
sums = sorted(sums.items(), key=lambda x: x[1], reverse=True)

for letter, _ in sums:
    print(letter, end="")

print()

    



