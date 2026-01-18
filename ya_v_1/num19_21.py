def f(s1, s2, m):
    if s1 + s2 >= 231:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(s1 + 4, s2, m - 1), f(s1, s2 + 4, m -1),
         f(s1*3, s2, m - 1), f(s1, s2*3, m - 1)]

    if m % 2 != 0:
        return any(h)
    else:
        return all(h)
        # return any(h)

print('19', [s2 for s2 in range(1, 218) if f(10, s2, 2)])
print('20', [s2 for s2 in range(1, 218) if f(10, s2, 3) and not f(10, s2, 1)])
print('21', [s2 for s2 in range(1, 218) if not f(10, s2, 2) and f(10, s2, 4)])