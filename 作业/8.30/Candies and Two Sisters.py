import math

t = int(input())
sum = []
for i in range(t):
    a = int(input())
    if a % 2 == 0:
        sum.append(a / 2 - 1)
    else:
        sum.append(a - 1 - a // 2)
for i in sum:
    print(int(i))