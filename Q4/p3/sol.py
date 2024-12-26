numbers = []

with open("../input.txt") as f:
    lines = f.readlines()
    for line in lines:
        num = int(line)
        numbers.append(num)

median = sorted(numbers)[len(numbers) // 2]

count = 0

for number in numbers:
    count += abs(number - median)

print(count)