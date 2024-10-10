# n = input()
# letters = list(n)
# n_1 = []
# for a in letters:
#     if a not in n_1:
#         n_1.append(a)
# if len(n_1) % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")
n = set()
n.update(input())
if len(n) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")