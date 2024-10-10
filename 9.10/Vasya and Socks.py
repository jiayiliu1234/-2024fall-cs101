# n, m = map(int, input().split())
# day = 0
# while True:
#     n -= 1
#     if n < 0:
#         break
#     day += 1
#     if day % m == 0:
#         n += 1
# print(day)
n,m = map(int, input().split())
t = n
while t//m>0:
        n += t//m
        t = t//m + t%m

print(n)