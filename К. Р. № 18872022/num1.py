from itertools import *

def f(x, y, z, w):
 return (x <= (y == w)) and (y == (w <= z))

d = set()
for i1, i2 in product([0,1], repeat=2):
    t = [(1, i1, 0, 1), (0, 0, i2, 0), (0, 0, 0, 1)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
                d.add(p)
print(*d)