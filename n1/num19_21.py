def f(s, m):
    if s <= 19:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s//3, m - 1)]

    if m % 2 != 0:
        return any(h)
    else:
        return all(h)

print('19)', [s for s in range(20, 100) if f(s, 2) and not f(s, 1)])
print('20)', [s for s in range(20, 100) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(20, 100) if f(s, 4) and not f(s, 2)])