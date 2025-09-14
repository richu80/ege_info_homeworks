from itertools import *
vsego = set()
sm = 0
for n in permutations('ПАРАБОЛА', 8):
    w = ''.join(n)
    vsego.add(w)

for i in vsego:
    i = i.replace('Р', 'П').replace('Б', 'П').replace('Л', 'П').replace('О', 'А')
    if 'АА' not in i and "ПП" not in i:
        sm += 1

print(sm)

#192