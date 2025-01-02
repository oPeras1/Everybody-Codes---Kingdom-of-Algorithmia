from collections import *

transform = dict()

with open("../input.txt") as f:
    for line in f:
        index, letters = line.split(":")
        letters = letters.strip()
        letters = letters.split(",")
        transform[index] = letters

def counter_fromkeys(iterable, v):
    new = Counter()
    for k in iterable:
        new[k] += v
    return new

final_counts = []

for letter in transform:
    counts = Counter([letter])

    for _ in range(20):

        newcount = Counter()

        for k,v in counts.items():
            newcount += counter_fromkeys(transform[k],v)

        counts = newcount
        
    final_counts.append(sum(counts.values()))

print(max(final_counts)-min(final_counts))