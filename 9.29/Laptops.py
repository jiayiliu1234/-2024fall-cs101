n = int(input())
laplops = []
flag = False
for _ in range(n):
    laplops.append(list(map(int, input().split())))
laplops.sort(key = lambda x: (x[0], -x[1]))
for i in range(n - 1):
    if laplops[i][1] > laplops[i + 1][1]:
        flag = True
        break
if flag:
    print('Happy Alex')
else:
    print('Poor Alex')