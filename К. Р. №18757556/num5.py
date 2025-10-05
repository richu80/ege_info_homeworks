from itertools import *
lst = 0
for i in product('13579', repeat=4):
    s1 = int(i[0]) + int(i[1])
    s2 = int(i[2]) + int(i[3])
    if s1 <= s2:
        r = str(s1) + str(s2)
    else:
        r = str(s2) + str(s1)
    if r == '616':
        lst += 1
        print(i)
print(lst)