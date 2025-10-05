
lst = []
for x in '0123456789abc':
    for y in '0123456789abc':
        n = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        if n%9 == 0:
            lst.append(n)
print(min(lst)//9)