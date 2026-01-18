count = 0
for i in range(1000, 10000):
    s = str(i)
    if len(set(s)) == len(s):
        s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')\
            .replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
        if '00' not in s and '11' not in s:
            count += 1
print(count)