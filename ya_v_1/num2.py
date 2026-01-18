from itertools import *
def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)

d = set()
for a1, a2 in product([0, 1], repeat=2):
    t = [(0, a1, 1, 0), (0, a2, 1, 0), (0, 1, 1, 1)]
    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                d.add(p)
        print(*d)
