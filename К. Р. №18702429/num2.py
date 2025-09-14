from itertools import *

def f(x, y, z, w):
 return ((y or z) <= (z and w)) == (not ((x and z) <= (w or y)))

d = set()
for i1, i2 in product([0,1], repeat=2):
    t = [(i1, 1, 1, 1), (0, 0, 0, i2), (1, 1, 0, 0)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                d.add(p)
print(*d)