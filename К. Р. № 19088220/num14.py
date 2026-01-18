lst = []
for x in '012345678':
    for y in '012345678':
        n = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if n % 61 == 0:
            lst.append(n)
print(min(lst)//61)