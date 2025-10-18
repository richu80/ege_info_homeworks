from itertools import *
vsego = set()
for n in product('012345678', repeat=5):
    w = ''.join(n)
    m = 9
    flag = True
    for i in w:
        if int(i) < int(m) and w[0] != '0':
            m = i
        else:
            flag = False
            break
    if flag:
        vsego.add(w)

print(len(vsego))