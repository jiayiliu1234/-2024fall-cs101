n = int(input())
num = 1
interval = []
for _ in range(n):
    x, y = map(int, input().split())
    interval.append([x, y])
interval.sort(key=lambda x:(-x[0], x[1]))
left = interval[0][0]
for a in interval:
    if a[1] < left:
        left = a[0]
        num += 1
print(num)