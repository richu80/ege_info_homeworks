from itertools import *
vsego = 0
for n in product('0123', repeat=3):
    w = ''.join(n)
    if int(w[0]) + int(w[-1]) > int(w[1]) and w[0] != '0':
        vsego += 1

print(vsego)