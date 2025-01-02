transform = dict()

with open("../input.txt") as f:
    for line in f:
        index, letters = line.split(":")
        letters = letters.strip()
        letters = letters.split(",")
        transform[index] = letters

string = ["Z"]

for i in range(10):
    lcl = []
    for char in string:
        lcl += transform[char]

    string = lcl

print(len(string))