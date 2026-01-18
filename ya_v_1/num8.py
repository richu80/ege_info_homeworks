from itertools import *
n = 0
lst = []
for i in product(sorted('аекптч'), repeat=7):
    w = ''.join(i)
    n += 1
    if w == 'аптечка' or w == 'печатка':
        print(n, w)
        lst.append(n)
print(lst[1] - lst[0] - 1)