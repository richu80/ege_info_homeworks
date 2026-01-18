import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n == 1:
        return 1
    else:
        return n - 2 + f(n - 1)
print(f(2023) - f(2021))