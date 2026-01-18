c = 0
for s in open('9.txt'):
    x = sorted([int(i) for i in s.split()])
    if x[0] == x[1] and x[2] == x[3] and x[0] + x[2] == 180:
        c += 1
print(c)