from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=None)
def getPower(src, nd_tgt):
    time = 0
    while True:
        tgt = (nd_tgt[0] - time, nd_tgt[1] - time)
        dx = tgt[0] - src[0]
        dy = tgt[1] - src[1]

        p = dx // 2
        if dx == dy and dx % 2 == 0:
            return (p + src[1], p * (1 + src[1]))


        t = dx - dy
        p = dy - dx // 2
        if dx % 2 == 0 and 0 < t <= p:
            return (p + src[1], p * (1 + src[1]))

        t = dx // 2 - 2 * dy // 3
        p = dy // 3
        if dy % 3 == 0 and dx % 2 == 0 and t > 0:
            return (p + src[1], p * (1 + src[1]))
        time += 1

with open('../input.txt') as f:
    lines = f.readlines()

    letters = [(0, 0), (0, 1), (0, 2)]

    meteors = []
    for l in lines:
        x, y = l.split(' ')
        meteors += [(int(x), int(y))]

    tot = 0
    for m in meteors:
        powers = []

        for l in letters:
            powers += [getPower(l, m)]
        tot += max(powers, key = lambda x: (x[0], -x[1]))[1]
    print(tot)