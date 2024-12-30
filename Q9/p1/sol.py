numbers = []

adders = [1, 3, 5, 10]

adders = adders[::-1]

with open("../input.txt") as f:
    lines = f.readlines()
    for line in lines:
        num = int(line)
        numbers.append(num)


def min_number(stamps, targets):
    results = {}
    total_beetles = 0

    max_brightness = max(targets)

    dp = [float('inf')] * (max_brightness + 1)
    dp[0] = 0

    backtrack = [-1] * (max_brightness + 1)

    for stamp in stamps:
        for brightness in range(stamp, max_brightness + 1):
            if dp[brightness - stamp] + 1 < dp[brightness]:
                dp[brightness] = dp[brightness - stamp] + 1
                backtrack[brightness] = stamp

    for target in targets:
        if dp[target] == float('inf'):
            results[target] = None
        else:

            combination = []
            current = target
            while current > 0:
                stamp_used = backtrack[current]
                combination.append(stamp_used)
                current -= stamp_used

            results[target] = combination
            total_beetles += len(combination)

    return total_beetles


total_beetles = min_number(adders, numbers)

print(total_beetles)




