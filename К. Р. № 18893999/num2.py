from itertools import *

def f(x, y, z, w):
 return ((x and (not y)) <= ((not z) or (not w))) and ((w <= z) or y)

d = set()
for i1, i2, i3, i4, i5, i6 in product([0,1], repeat=6):
    t = [(1, i1, 1, 1), (0, i2, i3, 0), (1, i4, i5, i6)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                d.add(p)
print(*d)