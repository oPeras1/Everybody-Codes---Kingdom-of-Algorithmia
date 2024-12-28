import more_itertools

G = """S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-"""

G = G.split('\n')
R = len(G)
C = len(G[0])

r,c,d = 0,0,1
D = [(0,-1),(1,0),(0,1),(-1,0)]
track_str = ''
done = False
i = 0

while not done:
    if len(track_str)>0 and G[r][c]=='S':
        break

    if done:
        break

    for new_d in [d, (d+3)%4, (d+1)%4]:
        rr = r+D[new_d][1]
        cc = c+D[new_d][0]

        if 0<=rr<len(G) and 0<=cc<len(G[rr]) and G[rr][cc]!=' ':
            track_str += G[rr][cc]

            r,c = rr,cc
            d = new_d

            i += 1
            break


actions_by_id = {}
data = open('../input.txt').read().strip()
for line in data.split('\n'):

    id_, actions = line.split(':')
    actions = actions.split(',')

    actions_by_id[id_] = actions

DP = {}
def score_one(actions):
    key = tuple(actions)

    if key in DP:
        return DP[key]
    
    power = 0
    score = 0
    
    i = 0

    for c in track_str:
        if c=='=' or c=='S':
            c = actions[i%len(actions)]

        if c=='+':
            power += 1

        elif c=='-':
            power -= 1

        else:
            assert c=='=' or c=='S', c

        score += power

        i += 1
    DP[key] = (score, power)
    return (score, power)

def score(actions, track, rounds):
    score = 0
    power = 10

    i = 0

    for _ in range(rounds):
        round_actions = actions[i:] + actions[:i]
        round_score, round_power = score_one(round_actions)

        score += round_score + power * len(track)
        power += round_power

        i = (i+len(track))%len(actions)

    return score

enemy_score = score(actions_by_id['A'], track_str, 2024)

ans = 0
opts = set(more_itertools.distinct_permutations('+++++---==='))


for i, opt in enumerate(opts):
    opt_score = score(opt, track_str, 2024)

    if opt_score > enemy_score:
        ans += 1

print(ans)