n = list(map(int, input().split()))
num = []
d = sum(n)
ans = 0
for i in range(10):
    num += [i] * n[i]
for i in range(d):
    ans += num[i] * 10 ** i
print(ans)