lst = []
for n in range(1, 100000):
    s = f'{n:b}'
    s = s[0:-1]
    if n % 2 == 1:
        s = s + '10'
    else:
        s = s + '01'
    r = int(s, 2)
    if r == 2018:
        print(n)
