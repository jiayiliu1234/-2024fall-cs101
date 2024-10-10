n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
distance = []
for i in range(len(a) - 1):
    distance.append((a[i + 1] - a[i]) / 2)
if a[0] != 0:
    distance.append(a[0])
if a[-1] != l:
    distance.append(l - a[-1])
d = max(distance)
print(f'{d:.10f}')