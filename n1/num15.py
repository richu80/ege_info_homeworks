from itertools import *
def f(x):
    p = 215 <= x <= 264
    q = 221 <= x <= 294
    a = a1 <= x <= a2
    return not (p <= ((not a) and q) <= (not p))

