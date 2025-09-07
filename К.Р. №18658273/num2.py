from itertools import *

def f(x, y, z, w):
    return (not (x <= z)) or (y == w) or y

d = set()
for i1, i2, i3, i4, i5, i6, i7 in product([0,1], repeat=7):
    t = [(1, 0, i1, i2), (i3, 1, 0, i4), (0, i5, i6, i7)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                d.add(p)
print(*d)

#zxyw