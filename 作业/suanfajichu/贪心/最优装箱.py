n, w = map(int, input().split())
wi = sorted(list(map(int, input().split())))
ans = 0
weight = 0
while w - wi[ans] >= 0:
    w -= wi[ans]
    weight += wi[ans]
    ans += 1
print(f'{ans} {weight}')