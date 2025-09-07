from itertools import *

s = 0

for i in product('кот', repeat=6):
    w = ''.join(i)
    if w.count('к') == 1:
        s += 1

print(s)

#192