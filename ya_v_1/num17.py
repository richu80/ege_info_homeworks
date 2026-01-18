x = [int(i) for i in open('17.txt')]
c = 0
mn = []
for k in range(2, len(x) - 3):
    p1 = x[k - 2] + x[k - 1]
    p2 = x[k] + x[k + 1]
    p3 = x[k + 2] + x[k + 3]
    if p2 > 0 and p1 > 0 and p3 > 0:
        if p2 > p1 and p2 > p3:
            c += 1
            mn.append(x[k] * x[k + 1])
print(c, min(mn))
