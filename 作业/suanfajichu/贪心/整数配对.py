n, m = map(int, input().split())
s = sorted(list(map(int, input().split())), reverse=True)
t = sorted(list(map(int, input().split())), reverse=True)
l = min(n, m)
i, j = 0, 0
num = 0
while i < n and j < m:
    if s[i] <= t[j]:
        num += 1
        i += 1
        j += 1
    else:
        i += 1
print(num)