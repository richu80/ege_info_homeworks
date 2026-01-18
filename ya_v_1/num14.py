# n = 18 * 7**108 - 5*49**76 + 343**35 - 50
def f(n):
    s = []
    while n < 0:
        s.append(n%49)
        n //= 49
    return s[::-1]
print(sum(f(abs(18 * 7**108 - 5*49**76 + 343**35 - 50)))