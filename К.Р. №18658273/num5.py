def cc(n):
    s = ''
    while n > 0:
        s = str( n%3 ) + s
        n //= 3
    return s

lst = []

for n in range(3, 10000):
    s = cc(n)
    if n % 3 == 0:
        s += s[-2:]
    else:
        s += cc((n % 3) * 5)
    r = int(s, 3)

    if r <= 173:
        lst.append(r)
print(max(lst))

#162