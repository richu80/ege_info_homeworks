# def f(s, m):
#     if s >= 40:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     h = [f(s + 4, m - 1), f(s*2, m -1), f(s + 1, m - 1)]
#
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)
#
# print("19)", [s for s in range(1, 40) if f(s, 2)])
# print("20)", [s for s in range(1, 40) if f(s, 3) and not f(s, 1)])
# print("21)", [s for s in range(1, 40) if f(s, 4) and not f(s, 2)])
#
# # 19) [720]
# # 20) [240, 719]
# # 21) [718]

print(5050**2 - 100*50**3)