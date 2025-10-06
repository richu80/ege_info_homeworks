sm = 0
for s in open('num7.txt'):
    x = sorted([int(i) for i in s.split()])
    if len(x) == len(set(x)) and (x[0] + x[-1])/2 > sum(x[1:-1])/4:
        sm += 1
print(sm)