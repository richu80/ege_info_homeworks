k = 0

for s in open('09 (1).txt'):
    x = sorted([int(i) for i in s.split()])
    p = [i for i in x if x.count(i) >= 2]
    np = [i for i in x if x.count(i) == 1]
    if p and np and sum(p)/len(p) < sum(np)/len(np):
        k += 1

print(k)