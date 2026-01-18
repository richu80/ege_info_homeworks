lst = []
count = 0
for s in open('9.txt'):
    count += 1
    x = [int(i) for i in s.split()]
    p = sorted([i for i in x if x.count(i) == 2])
    np = [i for i in x if x.count(i) == 1]
    if len(p) == 6 and len(np) == 2 and (p[-1] - p[0])**2 > (np[0]**2 + np[1]**2)*2:
        lst.append(count)
print(max(lst))