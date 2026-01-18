from itertools import *
t = '14,24,26,34,37,45,46,47,57'
g = 'ab,bc,bd,be,bf,bg,cd,ef,fg'
t = t + ',' + t[::-1]
g = g + ',' + g[::-1]

s = 'abcdefg'

for ss in permutations(s):
    nt = g
    for i, v in enumerate(ss):
        nt = nt.replace(v, str(i + 1))
    if set(nt.split(',')) == set(t.split(',')):
        print(ss)
