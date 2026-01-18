l = []
def f(n):
    s = ''
    while n > 0:
        s = str(n%5) + s
        n //= 5
    return s

for n in range(1, 10000):
    s = f(n)
    if n % 25 == 0:
        s = s[-3::] + s
    else:
        s += f(n%25)
    r = int(s, 5)

    if n == 25 or n == 26:
        print(n, r, s)
    if r > 10000:
        l.append(n)
print(min(l))