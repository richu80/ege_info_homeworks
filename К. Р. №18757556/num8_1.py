from itertools import *
counter = 0
for i in product('АВЛОР', repeat=4):
    w = ''.join(i)
    counter += 1
    if w[0] == 'Л':
        print(counter)
        break