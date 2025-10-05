from itertools import *

def f(x, y, z, w):
    return ((x or (not y)) and ((not z) == w)) <= (y and z)

d = set()
for i1, i2, i3, i4 in product([0, 1], repeat=4):
    t = [(1, i1, 1, 1), (0, 0, i2, 0), (0, i3, i4, 1)]
    if len(set(t)) == len(t):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                d.add(p)
print(d)

#yzwx