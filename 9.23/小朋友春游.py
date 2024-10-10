n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
my_class = []
other_class = []
for i in range(1, n + 1):
    if i not in a:
        my_class.append(i)
for i in a:
    if i > n:
        other_class.append(i)
print(*my_class)
print(*other_class)

# n = int(input())
# a = list(map(int, input().split()))
# a = sorted(a)
# my_class = []
# other_class = []
# for i in a:
#     if i <= n:
#         my_class.append(i)
#     else:
#         other_class.append(i)
# for i in range(1, n + 1):
#     if i not in my_class:
#         print(i, end=' ')
# print()
# for i in other_class:
#     print(i, end=' ')