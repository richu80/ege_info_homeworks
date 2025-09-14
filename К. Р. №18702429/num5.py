lst = []
for n in range(1, 100000):
    s = f'{n:b}'
    for i in range(2):
        s += str(sum(map(int, list(s)))%2)
    r = int(s, 2)

    if r < 100:
        lst.append(r)

print(max(lst))

#96

