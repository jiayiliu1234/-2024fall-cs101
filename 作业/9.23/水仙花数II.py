a, b = map(int, input().split())
ans = []
for i in range(a, b + 1):
    if (i // 100) ** 3 + ((i - 100 * (i // 100)) // 10) ** 3 + (i - 100 * (i // 100) - 10 * ((i - 100 * (i // 100)) // 10)) ** 3 == i:
        ans.append(i)
if len(ans) == 0:
    print('NO')
else:
    print(*ans)