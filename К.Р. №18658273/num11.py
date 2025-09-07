from math import *


char1 = ceil(log2(10 + 26))
lk = ceil(char1 * 13 / 8)
char2 = ceil(log2(61))
char3 = ceil(log2(12))
sd = ceil((char2 + char3)/8)

print(lk + sd)

#12