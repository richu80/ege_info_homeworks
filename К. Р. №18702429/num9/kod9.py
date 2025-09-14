sm = 0
for s in open('09.txt'):
    x = sorted([int(i) for i in s.split()])
    pov = sorted([i for i in x if x.count(i) > 1])
    if len(set(x)) < len(x) and x.count(x[-1]) == 1 and sum(pov) < x[-1]:
        sm += 1
print(sm)

#884