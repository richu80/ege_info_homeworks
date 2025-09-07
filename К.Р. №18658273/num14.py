def cc(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n //= 9
    return s

n = cc(81**17 + 3**24 - 45)

print(n.count('8'))

#10