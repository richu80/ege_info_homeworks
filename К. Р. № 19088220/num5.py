lst = []
for n in range(1, 1000):
    s = f'{n:b}'
    sm = sum(list(map(int, s)))
    if sm % 2 == 1:
        s = s + '11'
    else:
        s = s + '00'
    r = int(s, 2)

    if r > 114:
        print(n, s, r)
        lst.append(r)
print(min(lst))