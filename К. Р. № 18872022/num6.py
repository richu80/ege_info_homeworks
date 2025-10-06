sm = 0
for s in open('num6.txt'):
    x = sorted([int(i) for i in s.split()])
    if x[0] + x[1] > x[2]  and x[0]**2 + x[1]**2 > x[2]**2:
        sm += 1
print(sm)