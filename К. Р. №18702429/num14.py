lst = []
for y in '0123456':
    for x in '0123456':
        sm = int(y + x + '320', 7) + int('1' + x + '3' + y + '3', 9)
        if sm % 181 == 0:
            lst.append(sm)
print(min(lst)/181)

#148