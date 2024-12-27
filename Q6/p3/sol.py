graph = {}

with open('../input.txt', 'r') as f:
    for line in f:
        node, children = line.strip().split(':')
        children = children.split(',')
        graph[node] = children

queue = [("RR", "RR")]

paths = set()

while queue != []:
    node, path = queue.pop(0)

    if node not in graph:
        paths.add(path)
        continue

    for child in graph[node]:

        if child in path:
            continue

        queue.append((child, path + "," + child))

answer: dict[str, int] = dict()

for path in paths:
    length = len(path)
    if length in answer:
        answer[length] += 1
    else:
        answer[length] = 1

for k, v in answer.items():
    if v == 1:
        for path in paths:
            if len(path) == k:
                answer = path.split(",")
                break

for char in answer:
    print(char[0], end="")

print()