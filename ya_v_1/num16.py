from functools import *
@lru_cache(None)
def f(n):
    if n > 10000:
        return 42
    if n <= 10000 and n % 2 != 0:
        return -(n + f(n + 1) + f(n + 3))
    else:
        return 2*n + f(n + 3) + f(n + 4) + f(n + 6)

for n in range(10001, 9994, -1):
    f(n)

print(f(9996) - f(9994))