transform = dict()

with open("../input.txt") as f:
    for line in f:
        index, letters = line.split(":")
        letters = letters.strip()
        letters = letters.split(",")
        transform[index] = letters

string = ["A"]

for i in range(4):
    lcl = []
    for char in string:
        lcl += transform[char]

    string = lcl

print(len(string))