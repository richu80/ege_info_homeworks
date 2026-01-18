def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
mx = []
for n in range(1, 10000):
    s = f(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s += f((n % 3)*4)
    r = int(s, 3)
    if n == 11 or n == 12:
        print(r)
    if r <= 250:
        mx.append(n)

print(max(mx))