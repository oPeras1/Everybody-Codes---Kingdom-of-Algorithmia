numbers = []

adders = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

with open("../input.txt") as f:
    numbers = [int(line.strip()) for line in f]


total = 0
max = max(numbers)

dp = [float('inf')] * (max + 1)
dp[0] = 0

for x in range(1, max+1):
    for stamp in adders:
        if x >= stamp:
            dp[x] = min(dp[x], dp[x - stamp] + 1)

for sparkball in numbers:
    min_sparkball = float("inf")

    lower = sparkball // 2
    higher = sparkball - lower

    for split in range(0, 51):
        min_sparkball = min(min_sparkball, dp[lower + split] + dp[higher - split])

    total += min_sparkball
print(total)