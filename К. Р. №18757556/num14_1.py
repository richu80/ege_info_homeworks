def cc(n):
    s = ''
    while n > 0:
        s = str( n%3 ) + s
        n //= 3
    return s
z = cc(9**8 + 3**5 - 2)
print(str(z).count('2'), z)