from math import *
for n in range(1, 1000):
    kod = log2(10 + 26 + 26)
    char = ceil(kod*n/8)
    if char*1000 <= 10*2**10:
        print(n)