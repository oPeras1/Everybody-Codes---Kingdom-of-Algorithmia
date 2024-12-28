calculations = {}

racetrack_ = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""

racetrack = []
rverse = []

k = 0
for line in racetrack_.split("\n"):
    if k == 0:
        racetrack.extend(line[1:])
    elif k != len(racetrack_.split("\n"))-1:
        racetrack.append(line[len(line)-1])
        rverse.append(line[0])
    else:
        #append the line in reverse
        racetrack.extend(line[::-1])
    k += 1

rverse = rverse[::-1]
racetrack.extend(rverse)
racetrack.append("=")


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

    i = 0
    for _ in range(10):
        for c in racetrack:
            valueracetrack = c

            sumvalue = 0
            if valueracetrack == "+":

                num += 1

            elif valueracetrack == "-":

                num -= 1

            else:
                
                k = (i)%len(calculations[letter])

                num += getsum(letter, k)
            
            sum += num
            i += 1
    
    sums[letter] = sum

#sort by max value to min value
sums = sorted(sums.items(), key=lambda x: x[1], reverse=True)

for letter, _ in sums:
    print(letter, end="")

print()

    



