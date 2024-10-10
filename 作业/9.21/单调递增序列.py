n = int(input())
a = list(map(int, input().split()))
check = True
for i in range(n - 1):
    if a[i + 1] < a[i]:
        check = False
if check:
    print('YES')
else:
    print('NO')