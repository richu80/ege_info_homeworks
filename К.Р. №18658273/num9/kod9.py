k = 0

for s in open('09.txt'):
    x = sorted([int(i) for i in s.split()])
    if len(set(x)) == len(x) and (x[0] + x[-1]) * 3 <= (x[1] + x[2] + x[3]) * 2:
        k += 1

print(k)

#853