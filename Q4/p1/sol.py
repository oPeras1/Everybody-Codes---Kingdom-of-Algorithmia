numbers = []

minimum = float('inf')
with open("../input.txt") as f:
    lines = f.readlines()
    for line in lines:
        num = int(line)
        numbers.append(num)
        minimum = min(minimum, num)

count = 0
for number in numbers:
    count += abs(minimum - number)

print(count)