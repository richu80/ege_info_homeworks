from itertools import *

def f(x, y, z, w):
 return (x or (not y)) and (not (y == z)) and (not w)

d = set()
for i1, i2, i3, i4 in product([0,1], repeat=4):
    t = [(1, 1, i1, i2), (i3, 1, 0, 0), (1, i4, 1, 0)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                d.add(p)
print(*d)