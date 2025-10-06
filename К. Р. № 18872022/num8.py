sm = 0
for s in open('num8.txt'):
    x = [int(i) for i in s.split()]
    p = [i for i in x if x.count(i) == 3]
    np = [i for i in x if x.count(i) == 1]
    if len(p) == 3 and len(np) == 3 and p[1] >= sum(np)/3:
        sm += 1
print(sm)