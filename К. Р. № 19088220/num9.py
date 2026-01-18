w = 0
for s in open('num9.txt'):
    x = sorted([int(i) for i in s.split()])
    p1 = x[0]*x[1]
    p2 = x[0]*x[2]
    p3 = x[1]*x[2]
    if p1 + p2 < p3 or p1 + p3 < p2 or p2 + p3 < p1:
        w += 1
print(w)