n = int(input())
interval = []
for _ in range(n):
    x, y = map(int, input().split())
    interval.append([x, y])
interval = sorted(interval, key=lambda x: (-x[0], x[1]))
num = 1
left = interval[0][0]
for i in range(1, len(interval)):
    if interval[i][1] <= left:
        num += 1
        left = interval[i][0]
print(num)